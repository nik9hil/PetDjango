#Import Dependencies
from django.contrib import admin
from django.conf.urls import url,include

#Mapping the urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Pet2Vet/', include('Pet2Vet.urls')),
]