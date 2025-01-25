
from django.shortcuts import render
import requests
from django.conf import settings

def index(request):
    weather_data = {}
    error_message = None
    if 'city' in request.GET:
        city = request.GET['city']
        api_key = settings.WEATHER_API_KEY
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['location']['name'],
                'country': data['location']['country'],
                'temperature': data['current']['temp_c'],
                'condition': data['current']['condition']['text'],
                'icon': data['current']['condition']['icon'],
            }
        else:
            error_message = "City not found. Please try again."
    return render(request, 'weather/index.html', {'weather': weather_data, 'error': error_message})


'''
import requests
from django.shortcuts import render

def index(request):
    weather_data = {}
    error_message = None
    if 'city' in request.GET:
        city = request.GET['city']
        api_key = 'eb883b18c4b84449835142546252401'
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['location']['name'],
                'country': data['location']['country'],
                'temperature': data['current']['temp_c'],
                'condition': data['current']['condition']['text'],
                'icon': data['current']['condition']['icon'],
            }
        else:
            error_message = "City not found. Please try again."
    return render(request, 'weather/index.html', {'weather': weather_data, 'error': error_message})
'''
'''
def index(request):
    weather_data = {}
    error_message = None
    if 'city' in request.GET:
        city = request.GET['city']
        api_key = 'your_api_key_here'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            error_message = "City not found. Please try again."
    return render(request, 'weather/index.html', {'weather': weather_data, 'error': error_message})
  '''


