from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
						url(r'^create_project$', views.create_project),
						url(r'^create_post$', views.create_post),
	)