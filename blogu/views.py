from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from blogu.models import Category,Blog,UserProfile,Comment,Follow
from blogu.forms import BlogForm
from django.template.defaultfilters import slugify
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.models import User
from datetime import datetime,date,tzinfo,timedelta

ZERO = timedelta(0)

class UTC(tzinfo):
  def utcoffset(self, dt):
    return ZERO
  def tzname(self, dt):
    return "UTC"
  def dst(self, dt):
    return ZERO

utc = UTC()

class MyRegistrationView(RegistrationView):
    def get(self):
        print self

def index(request):
    if request.method=="POST":
        blog_text=request.POST.get('blog_text')
        return render(request,'blogu/add_blog.html',{'blog_text':blog_text})
    blog_list = Blog.objects.order_by('-likes')[:10]
    show=[True]*len(blog_list)
    try:
        user1=User.objects.get(username=request.user)
        user2=UserProfile.objects.get(user=user1)
        liked_blogs_list=user2.liked_blogs.all()
        #print len(blog_list)
        for i in range(0,len(blog_list)):
            for lb in liked_blogs_list:
                if lb == blog_list[i]:
                    show[i]=False
                    break
                else:
                    show[i]=True
    except:
        pass
    context_dict = {}
    #print datetime.now()
    #print show
    context_dict['blogs']=blog_list
    comment_matrix=[]
    for blog in blog_list:
        comment_matrix.append(Comment.objects.filter(comment_to=blog).order_by('-likes')[:5])
    context_dict['comments']=comment_matrix
    b_time=[]
    for b in blog_list:
        days=(datetime.now(utc)-b.datetime_added).days
        seconds=(datetime.now(utc) - b.datetime_added).seconds
        minutes=seconds/60
        hours=minutes/60
        if  days>= 1:
            b_time.append(str(days)+" days ago")
        elif minutes>60:
            b_time.append(str(hours)+" hours ago")
        elif seconds>60:
            b_time.append(str(minutes)+" minutes ago")
        else:
            b_time.append("Just now")
    zipped_data=zip(blog_list,b_time,show)
    #print zipped_data
    context_dict['zipped_data']=zipped_data
    response = render(request,'blogu/index.html',context_dict)
    return response

def profile(request):
	pass

def category(request,category_name_slug):

    context_dict = {}
    context_dict['result_list']=None
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name']=category.name
        blogs = Blog.objects.filter(category=category).order_by('-likes')
        context_dict['blogs']=blogs
        context_dict['category']=category
        context_dict['category_name_slug']=category.slug
    except Category.DoesNotExist:
        context_dict['category_name']=category_name_slug
        pass
    b_time=[]
    for b in blogs:
        days=(datetime.now(utc)-b.datetime_added).days
        seconds=(datetime.now(utc) - b.datetime_added).seconds
        minutes=seconds/60
        hours=minutes/60
        if  days>= 1:
            b_time.append(str(days)+" days ago")
        elif minutes>60:
            b_time.append(str(hours)+" hours ago")
        elif seconds>60:
            b_time.append(str(minutes)+" minutes ago")
        else:
            b_time.append("Just now")
    zipped_data=zip(blogs,b_time)
    context_dict['zipped_data']=zipped_data

    return render(request,'blogu/category.html',context_dict)


def get_category_list(max_results=0,startswith=''):
    cat_list=[]
    if startswith=='':
        cat_list = Category.objects.all().order_by('name')
    elif startswith:
        #print "Hello"
        cat_list = Category.objects.filter(name__istartswith=startswith)
        #print cat_list1
    if max_results>0:
        if len(cat_list)>max_results:
            cat_list=cat_list[:max_results]
    return cat_list

def blog(request,blog_title_slug):
    b=None
    c=None
    b_time=None
    try:
        b=Blog.objects.get(slug=blog_title_slug)
        c=Comment.objects.filter(comment_to=b).order_by('-likes')
    except Blog.DoesNotExist:
        pass
    days=(datetime.now(utc)-b.datetime_added).days
    seconds=(datetime.now(utc) - b.datetime_added).seconds
    minutes=seconds/60
    hours=minutes/60
    if  days>= 1:
        b_time=str(days)+" days ago"
    elif minutes>60:
        b_time=str(hours)+" hours ago"
    elif seconds>60:
        b_time=str(minutes)+" minutes ago"
    else:
        b_time="Just now"
    return render(request,'blogu/blog.html',{'blog':b,'comments':c,'b_time':b_time})


@login_required
def like_category(request):
    if request.method=="GET":
        category_id=request.GET["category_id"]
        category1=Category.objects.get(id=int(category_id))
        category1.likes+=1
        category1.save()
        user1=User.objects.get(username=request.user)
        user2=UserProfile.objects.get(user=user1)
        user2.liked_categories.add(category1)
        user2.save()
        return HttpResponse(category1.likes)

def suggest_category(request):
    str=request.GET["query_string"]
    #print str
    result=get_category_list(100,str)
    cat_list=[]
    for name in result:
        cat=Category.objects.get(name=name)
        cat_list.append(cat)
    #print cat_list
    return render(request,'blogu/category_list.html',{'cats':cat_list})
    #return HttpResponse(cat_list)

@login_required
def like_blog(request):
    if request.method=="GET":
        blog_id=request.GET["blog_id"]
        blog=Blog.objects.get(id=int(blog_id))
        blog.likes+=1
        blog.save()
        #print request.user
        user1=User.objects.get(username=request.user)
        user2=UserProfile.objects.get(user=user1)
        user2.liked_blogs.add(blog)
        user2.save()
        return HttpResponse(blog.likes)

def add_blog(request,category_name_slug):
    try:
        cat=Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat=None

    if request.method=="POST":
        #print "hello again"
        form=BlogForm(request.POST)
        if form.is_valid():
            if cat:
                blog1=form.save(commit=False)
                blog1.written_by=request.user
                blog1.category=cat
                blog1.likes=0
                blog1.views=0
                blog1.datetime_added=datetime.now()
                #print blog1.title
                blog1.save()
                return blog(request,slugify(blog1.title))
        else:
            print form.errors
    else:
        form = BlogForm()

    context_dict={'form':form,'category':cat}
    return render(request,'blogu/add_blog.html',context_dict)

def login_and_signup(request):
    if request.method == 'POST':
        login_statement=None
        signup_statement=None
        login_username = request.POST.get('login_username')
        if login_username:
            login_password = request.POST.get('login_password')
            if not login_username:
                login_statement="Please enter the username"
            if not login_password and login_username:
                login_statement ="Please enter the password"
            #if username and password:
             #   us = UserProfile.objects.get(user=username)
              #  if not us:
               #     return HttpResponse("There is no user with that username")
            user = authenticate(username = login_username,password=login_password)
            if user and login_username and login_password:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/blogu/')
                else:
                    return HttpResponse("Your Nblik account is disabled.")
            else:
                print "Invalid login details: {0}, {1}".format(login_username,login_password)
                login_statement="Invalid username password combination"
        else:
            registered = False
            signup_username = request.POST.get('signup_username')
            signup_email = request.POST.get('signup_email')
            signup_password1 = request.POST.get('signup_password1')
            signup_password2 = request.POST.get('signup_password2')
            if signup_password1!=signup_password2:
                signup_statement="password not same"
            else:
                user=User.objects.create_user(username=signup_username,email=signup_email)
                user.set_password(signup_password1)
                user.save()
                user1=User.objects.get(username=signup_username)
                registered = True
                profile=UserProfile(user=user1,level=1)
                profile.save()
                up_follow=Follow(userprofile=user1)
                up_follow.save()
                user1 = authenticate(username = signup_username,password=signup_password1)
                #user1 = authenticate(username = signup_username,password=signup_password1)
                print user1
                login(request,user1)
                return HttpResponseRedirect('/blogu/')
                #return render(request,'blogu/signup2.html',{'username':signup_username})

        return render(request,'blogu/login.html',{'login_statement':login_statement,'signup_statement':signup_statement})
    else:
        return render(request,'blogu/login.html',{})
