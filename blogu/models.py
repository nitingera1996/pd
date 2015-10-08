from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if(self.likes<0):
            self.likes=0
        super(Category, self).save(*args,**kwargs)

    def __unicode__(self):
	    return self.name

class Blog(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    written_by=models.ForeignKey(User)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    #comments=models.ManyToManyField(Comment)
    text = models.TextField()
    likes=models.IntegerField(default=0)
    datetime_added=models.DateTimeField(default=datetime.now())
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if(self.likes<0):
            self.likes=0
        super(Blog, self).save(*args,**kwargs)

    def __unicode__(self):
        return self.title

        
class Tag(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category)
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='profile_images',blank=True)
    liked_blogs=models.ManyToManyField(Blog)
    liked_categories=models.ManyToManyField(Category)
    level=models.IntegerField(default=1)
    date_registered=models.DateTimeField(default=datetime.now())
    google_id=models.CharField(null=True,blank=True,unique=True,max_length=100)
    profile_tag_line=models.CharField(max_length=300,null=True,blank=True)
    languages=models.IntegerField(default=1)#English=1,Hindi=2,English And Hindi both =3
    followed_tags=models.ManyToManyField(Tag)
    def __unicode__(self):
        return self.user.username

class Comment(models.Model):
    comment_text=models.TextField()
    comment_by=models.ForeignKey(User)
    comment_to=models.ForeignKey(Blog)
    likes=models.IntegerField(default=0)
    def __unicode__(self):
        return self.comment_text

class Follow(models.Model):
    userprofile=models.OneToOneField(User)
    followed=models.ManyToManyField(UserProfile)
    followers=models.IntegerField(default=0)
    no_followed=models.IntegerField(default=0)
    def __unicode__(self):
        return self.userprofile.username
