from django.conf.urls import patterns, url
from blogu import views

urlpatterns = patterns('',
        url(r'^$',views.index,name='index'),
        url(r'^profile/$',views.profile,name="profile"),
		url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.category,name ="category"),
        url(r'^blog/(?P<blog_title_slug>[\w\-]+)/$',views.blog,name="blog"),
		)