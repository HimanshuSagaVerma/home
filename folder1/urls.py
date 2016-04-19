from django.conf.urls import url
from folder1 import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^index1/(?P<number>\d+)/$', views.index1),
	url(r'^first_api/$', views.first_api)
]