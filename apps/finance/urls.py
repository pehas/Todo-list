from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^category/(?P<id>\d+)/$', views.category, name='category'),
]
