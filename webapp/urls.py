from django.conf.urls import url
from . import views
from webapp.feeds import LatestNotificationFeed

urlpatterns = [

    url(r'^user_home$', views.index, name='index'),

    url(r'latest/ntfc',LatestNotificationFeed(),name='rss'),

    url(r'^uploadmenu/',views.uploadmenu,name="upload-menu"),
    url(r'^help/$',views.contact,name="contact"),

    url(r'^$', views.home, name='home'),
    url(r'^pre_login/$', views.pre_login, name='pre_login'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^register/$', views.register, name='register'),

    url(r'^messages_all/$', views.messages_all, name='messages_all'),
    url(r'^messages_add/$', views.add_message, name='add_message'),
    url(r'^message/(?P<mid>\d+)/$', views.message, name="message"),

    url(r'^notification_all/$', views.notification_all, name='notification_all'),
    url(r'^notification_add/$', views.add_notification, name='add_notification'),
    url(r'^notification/(?P<nid>\d+)/$', views.notification, name="notification"),

    url(r'^vid_all/$', views.vid_all, name='vid_all'),
    url(r'^vid/(?P<vid_id>\d+)/$', views.vid, name="vid"),
    url(r'^vid_add/$',views.addvid,name="vid_add"),
    url(r'^search/$',views.search,name="search"),
    url(r'^user_logout/$', views.user_logout, name="user_logout"),
    url(r'^delete_vid/(?P<vid_id>[0-9]+)/$', views.delete_vid, name='delete_vid'),

    url(r'^img_all/$', views.img_all, name='img_all'),
    url(r'^img/(?P<img_id>\d+)/$', views.img, name="img"),
    url(r'^img_add/$', views.addimg, name="img_add"),
    url(r'^delete_img/(?P<img_id>[0-9]+)/$', views.delete_img, name='delete_img'),

    url(r'^addsong/$',views.addsong,name="addsong"),
    url(r'^album_all/$', views.album_all, name='album_all'),
    url(r'^album/(?P<s_id>\d+)/$', views.album, name="album"),
    url(r'^addalbum/$',views.addalbum,name="addalbum"),

    url(r'^file_all/$', views.file_all, name='file_all'),
    url(r'^file/(?P<file_id>\d+)/$', views.file, name="message"),
    url(r'^file_add/$', views.addfile, name="file_add"),
    url(r'^delete_file/(?P<file_id>[0-9]+)/$', views.delete_file, name='delete_file'),

]
