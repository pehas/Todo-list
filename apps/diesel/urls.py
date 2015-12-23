from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.topics, name='diesel_up_topics'),

	url(r'^up/(?P<id>\d+)/$', views.up_force, name='diesel_up_force'),

	# url(r'^time/$', views.up_time, name='diesel_up_time'),

	url(r'^add/$', views.add, name='diesel_up_add'),
	url(r'^edit/(?P<id>\d+)/$', views.edit, name='diesel_up_edit'),
	url(r'^deleted/(?P<id>\d+)/$', views.deleted, name='topic_deleted'),
]
