from django.urls import path
from weather.views import WeatherView
from weather.views import WeatherPost


urlpatterns = [
    path('gerenciar', WeatherView.as_view(), name='Weather View'),
    path('forms', WeatherPost.as_view(), name='Weather Post'),

]
