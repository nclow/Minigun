from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^email/$', views.email, name='email'),
]