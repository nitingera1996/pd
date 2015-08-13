from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from blogu.models import Category,Blog,UserProfile,Comment
#from blogu.forms import CategoryForm,PageForm,UserForm,UserProfileForm
from django.template.defaultfilters import slugify
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.models import User


class MyRegistrationView(RegistrationView):
    def get(self):
        print self
		
def index(request):
    #request.session.set_test_cookie()
    context_dict = {}
    blog_list = Blog.objects.order_by('-likes')[:10]
    context_dict['blogs']=blog_list
    comment_matrix=[]
    for blog in blog_list:
        comment_matrix.append(Comment.objects.filter(comment_to=blog).order_by('-likes')[:5])
    context_dict['comments']=comment_matrix
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
        return render(request,'blogu/category.html',context_dict)
    except Category.DoesNotExist:
        context_dict['category_name']=category_name_slug
        pass
	return render(request,'rango/category.html',context_dict)


def get_category_list(max_results=0,startswith=''):
    cat_list=[]
    if startswith:
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
    try:
        b=Blog.objects.get(slug=blog_title_slug)
        c=Comment.objects.filter(comment_to=b).order_by('-likes')
    except Blog.DoesNotExist:
        pass
    return render(request,'blogu/blog.html',{'blog':b,'comments':c})

