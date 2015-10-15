from django.conf.urls import patterns, url
from blogu import views

urlpatterns = patterns('',
        url(r'^$',views.index,name='index'),
        url(r'^profile/$',views.profile,name="profile"),
		url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.category,name ="category"),
        url(r'^blog/(?P<blog_title_slug>[\w\-]+)/$',views.blog,name="blog"),
        url(r'^like_category/$',views.like_category,name="like_category"),
        url(r'^suggest_category/$',views.suggest_category,name="suggest_category"),
        url(r'^like_blog/$',views.like_blog,name="like_blog"),
        url(r'^(?P<category_name_slug>[\w\-]+)/add_blog/$',views.add_blog,name="add_blog"),
        url(r'^login_signup/',views.login_and_signup,name='login_signup'),
        url(r'^search_top/$',views.search_top,name='search_top'),
        url(r'^logout/$',views.logout,name='logout'),
        url(r'^google_login/$',views.google_login,name='google_login'),
        url(r'^follow_user/$',views.follow_user,name="follow_user"),
        url(r'^comment/$',views.comment,name='comment'),
        url(r'^add_propic/',views.add_propic,name="add_propic"),
		)
