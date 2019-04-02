#Import Dependency
from django.contrib import admin
from .models import Volunteer,Vet,DonateForm,FirstAid,AdoptForm

# Register your models here.
admin.site.register(Volunteer)
admin.site.register(Vet)
admin.site.register(DonateForm)
admin.site.register(FirstAid)
admin.site.register(AdoptForm)