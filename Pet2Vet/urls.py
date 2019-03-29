#Import Dependencies
from django.contrib import admin
from django.conf.urls import url
from . import views

#Mapping the urls
urlpatterns = [
    url(r'^$', views.index, name='index'),
]