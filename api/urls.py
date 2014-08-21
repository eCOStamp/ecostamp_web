from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
    url(r'^dummy/$', views.dummy, name="dummy"),
    url(r'^stamp/(?P<key>\w+)/$', views.stamp, name="stamp"),
)
