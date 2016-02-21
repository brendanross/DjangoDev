from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^poll/$', views.poll_list, name='poll_list'),
    url(r'^poll/new/$', views.poll_new, name='poll_new'),
]