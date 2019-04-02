#Import Dependencies
from django.db import models

# Create your models here.
class Volunteer(models.Model):
    yourname = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=150,blank=True)
    phonenumber = models.CharField(max_length=10,blank=True)
    city = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.yourname


class Vet(models.Model):
    name = models.CharField(max_length=100,blank=False)
    city = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=100,blank=False)
    phonenumber = models.CharField(max_length=10,blank=False)
    fees = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name

class DonateForm(models.Model):
    name = models.CharField(max_length=100,blank=False)
    city = models.CharField(max_length=100,blank=False)
    phonenumber = models.CharField(max_length=10,blank=False)

    def __str__(self):
        return self.name

class FirstAid(models.Model):
    title = models.CharField(max_length=100,blank=False)
    video = models.CharField(max_length=100,blank=False)
    
    def __str__(self):
        return self.title

class AdoptForm(models.Model):
    name = models.CharField(max_length=100,blank=False)
    phonenumber = models.CharField(max_length=10,blank=False)
    email = models.CharField(max_length=100,blank=False)
    city = models.CharField(max_length=100,blank=False)
    animal = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.name