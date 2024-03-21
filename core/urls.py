from django.urls import path
from weather.views import WeatherView
from weather.views import WeatherPost


urlpatterns = [
    path('visualizar', WeatherPost.get, name='Weather View'), 
    path('', WeatherPost.post, name='Weather Post'),

]
