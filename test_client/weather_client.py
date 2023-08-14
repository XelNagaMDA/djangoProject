import requests

url = 'http://localhost:8000/weather/get/Brasov'

response = requests.get(url)
print(response.status_code)
if response.status_code == 200:
    print(response.json())