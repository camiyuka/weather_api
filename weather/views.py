from django.views import View
from django.shortcuts import render, redirect
from .models import WeatherEntity
from .repositories import WeatherRepository
from .serializers import WeatherSerializer
from django import forms

class WeatherView(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weathers_queryset = repository.getAll()
        weathers_serializer = WeatherSerializer(weathers_queryset, many=True)
        weathers_data = weathers_serializer.data
        return render(request, "gerenciar_previsoes.html", {"weathers": weathers_data})

class WeatherPost(View):
    class WeatherForm(forms.Form):
        temperature = forms.FloatField()
        date = forms.DateField()
        city = forms.CharField(max_length=100)
        atmospheric_pressure = forms.FloatField()
        humidity = forms.FloatField()
        weather = forms.CharField(max_length=100)

    def get(self, request):
        form = self.WeatherForm()
        return render(request, 'weather_form.html', {'form': form})

    def post(self, request):
        form = self.WeatherForm(request.POST)
        if form.is_valid():
            temperature = form.cleaned_data['temperature']
            date = form.cleaned_data['date']
            city = form.cleaned_data['city']
            atmospheric_pressure = form.cleaned_data['atmospheric_pressure']
            humidity = form.cleaned_data['humidity']
            weather = form.cleaned_data['weather']

            # Salvar os dados no banco de dados
            WeatherEntity.objects.create(
                temperature=temperature,
                date=date,
                city=city,
                atmospheric_pressure=atmospheric_pressure,
                humidity=humidity,
                weather=weather
            )
            # Redirecionar para a página de gerenciamento de previsões
            return redirect('Weather View')
        else:
            # Se houver erros de validação, renderizar novamente o formulário com os erros
            return render(request, 'weather_form.html', {'form': form})
