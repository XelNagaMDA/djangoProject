import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

"""@api_view(["GET"])
def get_weather(request, city_name):
    # TODO: Add code (that works) that will fidn the weather for the city with the city name
    # If the city is invalid (or no weather can be found) return the appropriate response code and response message
    return Response(status=status.HTTP_200_OK, data=f'Sunny in {city_name}')
"""

"""url = "https://weatherapi-com.p.rapidapi.com/ip.json"

querystring = {"q": "<REQUIRED>"}

headers = {
    "X-RapidAPI-Key": "6fe88db82dmsh7ef124648db3c6dp1399e5jsn8bc2bf5ef176",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests


@api_view(["GET"])
def get_weather(request, city_name):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": city_name}

    headers = {
        "X-RapidAPI-Key": "6fe88db82dmsh7ef124648db3c6dp1399e5jsn8bc2bf5ef176",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    weather_data = response.json()

    if 'error' in weather_data:
        error_message = weather_data['error']['message']
        return Response(status=status.HTTP_400_BAD_REQUEST, data=error_message)

    city = weather_data.get('location', {}).get('city', 'Unknown City')
    condition = weather_data.get('current', {}).get('condition', {}).get('text', 'Unknown Condition')

    response_data = {
        "city": city,
        "condition": condition,
    }

    return Response(status=status.HTTP_200_OK, data=response_data)
