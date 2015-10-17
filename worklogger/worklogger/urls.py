from django.conf.urls import  include, url, patterns

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'worklogger.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                    url(r'^feed/', include('feed.urls')),
				    url(r'^admin/', include(admin.site.urls)),
				    url(r'^create_post/', include('create_post.urls')),
				    url(r'^first_page/', include('first_page.urls')),
    				)
	

