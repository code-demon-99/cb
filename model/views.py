from django.shortcuts import render
import pandas as pd
from django.views.generic import TemplateView


def home_view(request):
    return render (request,'home.html')


