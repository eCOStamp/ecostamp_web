from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
    url(r'^dummy/$', views.dummy, name="dummy"),
    url(r'^register/$', views.register, name="register"),
    url(r'^collect/$', views.collect, name="collect"),
    url(r'^stamp/(?P<key>\w+)/$', views.stamp, name="stamp"),
    url(r'^user/(?P<username>\w+)/$', views.user, name="user"),
)
