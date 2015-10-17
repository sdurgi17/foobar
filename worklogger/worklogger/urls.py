from django.conf.urls import  include, url

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^first_page/', include('first_page.urls')),
]

