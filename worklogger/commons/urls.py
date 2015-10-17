from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
urlpatterns = patterns(
    '',
    url(r'^$', 'worklogger.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    #url(r'^$', 'django_social_app.views.login'),
    #url(r'' , views.login),
#    url(r'^home/$', 'django_social_app.views.home'),
#    url(r'^logout/$', 'django_social_app.views.logout'),
)
