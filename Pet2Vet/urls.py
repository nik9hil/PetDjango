#Import Dependencies
from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import path,include

#Mapping the urls
urlpatterns = [
    # /Pet2Vet/
    url(r'^$', views.home, name='home'),

    # /Pet2Vet/about/
    url(r'about/$', views.about, name='about'),

    # /Pet2Vet/ngo/
    url(r'ngo/$', views.ngo, name='ngo'),

    # /Pet2Vet/doctors/
    url(r'doctors/$', views.doctors, name='doctors'),

    # /Pet2Vet/adopt/
    url(r'adopt/$', views.adopt, name='adopt'),

    # /Pet2Vet/firstaid/
    url(r'firstaid/$', views.firstaid, name='firstaid'),

    # /Pet2Vet/location/
    url(r'location/$', views.location, name='location'),

    # /Pet2Vet/contact/
    url(r'contact/$', views.contact, name='contact'),

    #DonateForm
    url(r'donate/entry/$',views.DonateEntry.as_view(),name='donate-entry'),

    # RegistrationForm
    #url(r'register/$', views.register, name='register'),

]