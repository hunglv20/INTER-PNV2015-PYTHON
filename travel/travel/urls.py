from django.conf.urls import patterns, include, url
# from django.conf import settings
# from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tourist/', include('tourist.urls', namespace="tourist")),
    url(r'^admin/', include(admin.site.urls)),
)