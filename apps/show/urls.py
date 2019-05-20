from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^newshow$', views.newshow),
    url(r'^addshow$', views.addshow),
    url(r'^show/(?P<num>\d+)$', views.show),
    url(r'^edit/(?P<num>\d+)$', views.edit),
    url(r'^destroy/(?P<num>\d+)$', views.destroy),
    url(r'^editshow$', views.editshow),
]