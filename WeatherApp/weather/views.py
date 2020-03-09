from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


# Create your views here.

def index(request):
    appid = "82b797b6ebc625032318e16f1b42c016"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    cities = City.objects.all()

    if (request.method == "POST"):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][-1]["icon"]
        }
        all_cities.append(city_info)

    conext = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', conext)
