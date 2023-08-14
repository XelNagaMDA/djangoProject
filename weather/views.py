import pydash
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
    city = pydash.get(weather_data, 'location.name', "Unknown City")
    condition = pydash.get(weather_data, 'current.condition.text', "Unknown Condition")
    response_data = {
        "city": city,
        "condition": condition,
    }
    return Response(status=status.HTTP_200_OK, data=response_data)