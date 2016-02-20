from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'', include('vote.urls')),
]
