# file to implement all the serializers
from rest_framework import serializers
from .models import CovidData

class CovidDataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CovidData
