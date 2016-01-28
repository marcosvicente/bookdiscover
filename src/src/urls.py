from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views 
from django.conf.urls.static import static
from django.conf import settings


from rest_framework import routers

from book.views import BookListView , BookDetailView 
from core.views import IndexListView


urlpatterns = [ 
    url(r'^$', IndexListView.as_view(), name='index'),       
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^book/$',  BookListView.as_view(), name='book'),
    url(r'^book/(?P<slug>[-\w]+)/$', BookDetailView.as_view(), name='book-detail'),



    



]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

