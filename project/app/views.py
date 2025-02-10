from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    city=request.GET.get('city')
    app_key = 'e8a5d5a6022f07752c3d8ef38ce151fd'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_key}&units=metric'
    api=requests.get(url).json()
    temperature=api['main']['temp']
    wind_speed=api['wind']['speed']
    name=api['name']
    country=api['sys']['country']
    print(temperature)
    weather=api["weather"]
    
    return render(request, 'index.html',{'temperature':temperature,'wind_speed':wind_speed,'name':name,'country':country})


# https://api.openweathermap.org/data/2.5/weather?q=bangalore&appid=e8a5d5a6022f07752c3d8ef38ce151fd&units=metric'