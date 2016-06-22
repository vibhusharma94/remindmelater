from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.rml import urls as apis_urls


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    # API Urls
    url(r'^api/', include(apis_urls)),

)
