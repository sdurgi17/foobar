from django.conf.urls import url ,include

from . import views

urlpatterns = [
   # url(r'^admin/', include(admin.site.urls)),
   url('', include('social.apps.django_app.urls', namespace='social')),
   url(r'^open',views.open_form),
   url(r'^signup', views.signup),
   url(r'^facebook', views.signup_facebook),
   url(r'^login', views.login),
   url(r'^logout',views.logout),

]