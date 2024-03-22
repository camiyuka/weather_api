from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import WeatherEntity
from .repositories import WeatherRepository
from .serializers import WeatherSerializer
from django import forms
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.http.response import HttpResponse

@csrf_exempt

class WeatherView(View):
    # get all
    def get(request):
        repository = WeatherRepository(collectionName='weathers')
        weathers_queryset = repository.getAll()
        weathers_serializer = WeatherSerializer(weathers_queryset, many=True)
        weathers_data = weathers_serializer.data
        return render(request, "gerenciar_previsoes.html", {"weathers": weathers_data})

    def return_form(request):
        return render(request, 'weather_form.html')

    def post(request):
        data = request.POST
        model = WeatherEntity(
            temperature=data['temperature'],
            atmospheric_pressure=data['atmospheric_pressure'],
            humidity=data['humidity'],
            weather=data['weather'],
            city=data['city']
        )

        serializer= WeatherSerializer(data=model.__dict__)
        if serializer.is_valid():
            document=serializer.validated_data
            repository= WeatherRepository('weathers')
            repository.insert(document)
            return render(request, "gerenciar_previsoes.html", {"weathers": [serializer.data]})
        else:
            return HttpResponse(serializer.errors)

            # Se houver erros de validação, renderizar novamente o formulário com os erros
        # return render(request, 'weather_form.html', {'form': form})

