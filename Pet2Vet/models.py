#Import Dependencies
from django.db import models
from django.urls import reverse

# Create your models here.
class VolunteerRegister(models.Model):  #used
    yourname = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=150,blank=True)
    phonenumber = models.CharField(max_length=10,blank=True)
    city = models.CharField(max_length=50,blank=True)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.yourname


class VetRegister(models.Model):    #used
    name = models.CharField(max_length=100,blank=False)
    city = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=100,blank=False)
    phonenumber = models.CharField(max_length=10,blank=False)
    fees = models.CharField(max_length=100,blank=True)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name

class DonateForm(models.Model): #used
    name = models.CharField(max_length=100,blank=False)
    city = models.CharField(max_length=100,blank=False)
    phonenumber = models.CharField(max_length=10,blank=False)
    email = models.EmailField(max_length=50,blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class FirstAid(models.Model):   #Used
    title = models.CharField(max_length=100,blank=False)
    video = models.CharField(max_length=100,blank=False)
    description = models.CharField(max_length = 1000, blank=False)
    
    def __str__(self):
        return self.title

class AdoptForm(models.Model):  #used
    name = models.CharField(max_length=100,blank=False)
    phonenumber = models.CharField(max_length=10,blank=False)
    email = models.CharField(max_length=100,blank=False)
    city = models.CharField(max_length=100,blank=False)
    animal = models.CharField(max_length=100,blank=False)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name

class NGO(models.Model):    #Used
    name = models.CharField(max_length=100,blank=False)
    phonenumber = models.CharField(max_length=10,blank=False)
    city = models.CharField(max_length=100,blank=False)
    map = models.CharField(max_length=1000,blank=False)

    def __str__(self):
        return self.name

class Doctors(models.Model):    #Used
    name = models.CharField(max_length=100,blank=False)
    location = models.CharField(max_length=100,blank=False)
    contact = models.CharField(max_length=10,blank=False)
    map = models.CharField(max_length=1000,blank=False)

    def __str__(self):
        return self.name

class Pets(models.Model):   #Used
    name = models.CharField(max_length=100,blank=False)
    city = models.CharField(max_length=100,blank=False)
    contact = models.CharField(max_length=10,blank=False)
    gender = models.CharField(max_length=10,blank=False)
    location = models.CharField(max_length=1000,blank=False)

    def __str__(self):
        return self.name

class NGORegister(models.Model):    #used
    name = models.CharField(max_length=100,blank=False)
    phonenumber = models.CharField(max_length=10,blank=False)
    city = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=50,blank=False)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name