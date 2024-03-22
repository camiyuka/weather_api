from django.urls import path
from weather.views import WeatherView

urlpatterns = [
    path('visualizar', WeatherView.get, name='get'), 
    path('', WeatherView.return_form, name='weather post'),

]
