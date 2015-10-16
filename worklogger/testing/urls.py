from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
						url(r'^test/$', views.test),
						url(r'^receive_message/$', views.receive_message)
	)
