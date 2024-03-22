from rest_framework import serializers
from .models import WeatherEntity

class WeatherSerializer(serializers.Serializer):
    temperature = serializers.FloatField()
    date = serializers.DateField(required=False)  
    city = serializers.CharField(max_length=100, required=False)
    atmospheric_pressure = serializers.FloatField( required=False)
    humidity = serializers.FloatField( required=False)
    weather = serializers.CharField(max_length=100, required=False)

           
        
    