#Import Dependencies
from django.db import models

# Create your models here.
class Volunteer(models.Model):
    yourname = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=150,blank=True)
    phonenumber = models.CharField(max_length=10,blank=True)
    city = models.CharField(max_length=50,blank=True)