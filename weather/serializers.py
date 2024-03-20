from rest_framework import serializers
from .models import WeatherEntity
from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    temperature = serializers.DecimalField(max_digits=5, decimal_places=2)
    date = serializers.DateField()
    city = serializers.CharField(max_length=100, required=False)
    atmosphericPressure = serializers.CharField(max_length=100, required=False)
    humidity = serializers.CharField(max_length=100, required=False)
    weather = serializers.CharField(max_length=100, required=False)

    def create(self, validated_data):
        return WeatherEntity(**validated_data)

    def update(self, instance, validated_data):
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.date = validated_data.get('date', instance.date)
        instance.city = validated_data.get('city', instance.city)
        instance.atmosphericPressure = validated_data.get('atmosphericPressure', instance.atmosphericPressure)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.weather = validated_data.get('weather', instance.weather)
        return instance

