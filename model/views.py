from django.shortcuts import render
import pandas as pd
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response
import pandas as pd
from . serializers import CovidDataSerializer
from . models import CovidData
def home_view(request):
    return render (request,'model/home.html')

def task2_view(request):
    return render (request,'model/task2.html')

def task3_view(request):
    return render (request,'model/task3.html')


class CovidDataViewSet(viewsets.ModelViewSet):
    queryset = CovidData.objects.all()
    serializer_class = CovidDataSerializer


class ResultOneViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        df=pd.read_csv('static/CSV/res1.csv')

        data={
            'state':list(df['DetectedState']),
            'labels':list(df['DetectedDistrict']),
            'male_count':list(df['MaleCount']),
            'female_count':list(df['FemaleCount'])
        }
        return Response(data)


class ResultTwoViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        df=pd.read_csv('static/CSV/res2.csv')

        data={
            'state':list(df['DetectedState']),
            'DateAnnounced': list(pd.to_datetime(df['DateAnnounced']))
        }
        return Response(data)



class ResultThreeViewSet(viewsets.ViewSet):
    """
    This api will list the data related to the task3 of the project
    """
    def list(self,request):
        df=pd.read_csv('static/CSV/res3.csv')
        df
        data={
            'state':list(df['DetectedState']),
            'labels':list(df['Statecode']),
            'count_of_people':list(df['no_people']),
            'percentage_people':list(df['PercentageofPeople'])
        }
        return Response(data)
