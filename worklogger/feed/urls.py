from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^get_user_projects$',
                           views.user_projects),
                       url(r'^get_project_tasks$',
                           views.project_tasks),
                       )
