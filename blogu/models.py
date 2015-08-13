from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


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
    image=models.ImageField(upload_to="blog_images",blank=True)
    image_description=models.TextField(default='')
    heading=models.TextField(default='')
    text = models.TextField()
    likes=models.IntegerField(default=0)
    date_added=models.DateField(default='2015-01-01')
    time_added=models.TimeField(default='00:00')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if(self.likes<0):
            self.likes=0
        super(Blog, self).save(*args,**kwargs)
		
    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images',blank=True)
    #blogs=models.ManyToManyField(Blog)
    level=models.IntegerField(default=1)
    date_registered=models.DateField()
    def __unicode__(self):
        return self.user.username
		
class Comment(models.Model):
    comment_text=models.TextField()
    comment_by=models.ForeignKey(User)
    comment_to=models.ForeignKey(Blog)
    likes=models.IntegerField(default=0)
    def __unicode__(self):
        return self.comment_text
	
