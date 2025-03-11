from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    re_path(r'^post/$', views.post_view, name='post_form'),
    re_path(r'^post/(?P<id>\d+)/$', views.post_view, name='post'),
    re_path(r'^profile/$', views.profile_view, name='profile_post'),
    re_path(r'^profile/(?P<username>[a-zA-Z]+)/$', views.profile_view,
            name='profile'),
    re_path(r'^event(?:/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2}))?/$',
            views.event_view, name='event'),

]
