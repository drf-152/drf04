from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include('api.urls')),

    url(r'^admin/', include(admin.site.urls)),
)