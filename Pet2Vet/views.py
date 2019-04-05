#Import Dependencies
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Volunteer

#Create your views here

def home(request):
    context = {}
    return render(request, 'Pet2Vet/home.html', context)

def about(request):
    context = {}
    return render(request, 'Pet2Vet/about.html', context)

def ngo(request):
    context = {}
    return render(request, 'Pet2Vet/ngo.html', context)

def doctors(request):
    context = {}
    return render(request, 'Pet2Vet/doctors.html', context)

def adopt(request):
    context = {}
    return render(request, 'Pet2Vet/adopt.html', context)

def firstaid(request):
    context = {}
    return render(request, 'Pet2Vet/firstaid.html', context)

def location(request):
    context = {}
    return render(request, 'Pet2Vet/location.html', context)

def contact(request):
    context = {}
    return render(request, 'Pet2Vet/contact.html', context)    

class VolunteerCreate(CreateView):
    template_name='Pet2Vet/home.html'
    model = Volunteer
    fields = ['yourname', 'email', 'phonenumber', 'city']