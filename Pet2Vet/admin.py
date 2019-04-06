#Import Dependency
from django.contrib import admin
from .models import VolunteerRegister,VetRegister,DonateForm,FirstAid,AdoptForm,NGO,Doctors,Pets

# Register your models here.
admin.site.register(VolunteerRegister)
admin.site.register(VetRegister)
admin.site.register(DonateForm)
admin.site.register(FirstAid)
admin.site.register(AdoptForm)
admin.site.register(NGO)
admin.site.register(Doctors)
admin.site.register(Pets)