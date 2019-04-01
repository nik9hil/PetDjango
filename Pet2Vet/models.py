#Import Dependencies
from django.db import models

# Create your models here.
class Volunteer(models.Model):
    yourname = models.CharField(max_length=100)
    email = models.EmailField(max_length=150,blank=True)
    phonenumber = models.CharField(max_length=10)
    city = models.CharField(max_length=50)