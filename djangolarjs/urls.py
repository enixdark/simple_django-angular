from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangolarjs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("apps.djangular.urls")),
    url(r'^', include("apps.snippets.urls")),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
