from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views 

urlpatterns = [ 
    url(r'^$', 'core.views.index', name='index'),
       
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

     url(r'^accounts/', include('registration.backends.default.urls')),

   
]
