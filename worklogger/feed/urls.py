from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^user_projects$',
                           views.user_projects, name='index'),
                       url(r'^project_tasks$',
                           views.project_tasks),
                       )
