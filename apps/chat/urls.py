from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.chat_form, name='chat_form'),
	url(r'^text/$', views.chat_text, name='chat_text'),
]
