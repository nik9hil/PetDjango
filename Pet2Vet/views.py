#Import Dependencies
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Volunteer,NGO,FirstAid,Doctors,Pets
from django.template import loader

#Create your views here

def home(request):
    context = {}
    return render(request, 'Pet2Vet/home.html', context)

def about(request):
    context = {}
    return render(request, 'Pet2Vet/about.html', context)

def ngo(request):
    all_ngo = NGO.objects.all()
    template = loader.get_template('Pet2Vet/ngo.html')
    context = {
        'all_ngo' : all_ngo,
    }
    return HttpResponse(template.render(context, request))

def doctors(request):
    all_doctors = Doctors.objects.all()
    template = loader.get_template('Pet2Vet/doctors.html')
    context = {
        'all_doctors' : all_doctors,
    }
    return HttpResponse(template.render(context, request))

def adopt(request):
    all_pets = Pets.objects.all()
    template = loader.get_template('Pet2Vet/adopt.html')
    context = {
        'all_pets' : all_pets,
    }
    return HttpResponse(template.render(context, request))

def firstaid(request):
    all_firstaid = FirstAid.objects.all()
    template = loader.get_template('Pet2Vet/firstaid.html')
    context = {
        'all_firstaid' : all_firstaid,
    }
    return HttpResponse(template.render(context,request))

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