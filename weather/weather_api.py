import requests


def get_ip():
    ip_address = input("Please input your IP: ")
    return ip_address


def weather_api():
    with open('weather_api.txt', 'r') as file:
        content = file.read()
        return content


def geolocation():
    url = "https://weatherapi-com.p.rapidapi.com/ip.json"

    querystring = {"q": get_ip()}

    headers = {
        "X-RapidAPI-Key": weather_api(),
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
    # location = response.json()
    # latitude = location['lat']
    # longitude = location['lon']
    # return latitude, longitude
