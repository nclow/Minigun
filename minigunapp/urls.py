from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^email/(?P<id>[0-9a-f]{24})/$', views.EmailDetail.as_view()),
    url(r'^email/$', views.EmailList.as_view()),
]
