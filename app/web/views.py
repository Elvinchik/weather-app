from django.shortcuts import render
from .forms import WeatherForms
import requests

from .models import WeatherModels
from django.http import HttpResponseRedirect
import pyowm

error_text = ""


def home(request):
    global error_text
    info = WeatherModels.objects.all()
    forms = WeatherForms(request.POST)

    api = "25a90ee8201bd5e280543e9f3cb5afa8"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=" + api

    owm = pyowm.OWM(api)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place("Москва")
    w = observation.weather

    res = requests.get(url.format("Москва")).json()
    error_text = ""

    temp = round(w.temperature('celsius')['temp'])
    icon = res["weather"][0]["icon"]

    if request.method == "POST":
        
        if forms.is_valid():
            data = forms.cleaned_data
            
            if data.get("city").lower() != "очистить":
                try:
                    city = data.get("city")
                    error_text = ""

                    observation = mgr.weather_at_place(city)
                    w = observation.weather

                    res = requests.get(url.format(city)).json()
                    icon = res["weather"][0]["icon"]

                    temp = round(w.temperature('celsius')['temp'])
                    WeatherModels.objects.create(
                        city=city,
                        temp=temp,
                        icon=icon
                    )
                    return HttpResponseRedirect("/")
                except Exception:
                    error_text = "Данного города не существует."
            else:
                info.delete()
                return HttpResponseRedirect("/")
    context = {
        "form": forms,
        "info": info,
        "temp": temp,
        "icon": icon,
        "error": error_text
    }
    return render(request, "index.html", context)