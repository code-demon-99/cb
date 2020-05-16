from django.contrib import admin
from django.contrib.admin import AdminSite
from . models import CovidData
from django.core import management
from django.shortcuts import redirect 

# Model Covid Data Admin  added here 
@admin.register(CovidData)
class CovidDataAdmin(admin.ModelAdmin):
   pass