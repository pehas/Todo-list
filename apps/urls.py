from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Home
    url(r'^$', 'apps.views.home', name='home'),
    url(r'^results/$', 'apps.views.todos', name='todos'),
    url(r'^(?P<id>\d+)/$', 'apps.views.del_todo', name='del_todo'),
    url(r'^done/(?P<id>\d+)/$', 'apps.views.done_todo', name='done_todo'),

	# Admin
	url(r'^admin/', include(admin.site.urls)),
)


# For serve static, media, templates in develop mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/templates/', document_root=settings.PROJECT_DIR + '/templates/')