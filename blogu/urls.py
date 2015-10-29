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
        url(r'^logout/$',views.user_logout,name='logout'),
        url(r'^google_login/$',views.google_login,name='google_login'),
        url(r'^follow_user/$',views.follow_user,name="follow_user"),
        url(r'^comment/$',views.comment,name='comment'),
        url(r'^discuss/$',views.discuss,name='discuss'),
        url(r'^discussions/$',views.discussions,name='discussions'),
        url(r'^new_discussion/$',views.new_discussion,name='new_discussion'),
        url(r'^discussion/(?P<discussion_slug>[\w\-]+)/$',views.discussion,name="discussion"),
<<<<<<< HEAD
        #url(r'^next_step/$',views.next_step,name='next_step'),
=======
        url(r'^next_step/$',views.next_step,name="next_step"),

>>>>>>> f32e647df28e39f98bdfdd3f18a29ee15160672c
		)
