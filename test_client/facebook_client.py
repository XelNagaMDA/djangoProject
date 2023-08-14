import requests

url = 'http://127.0.0.1:8000/'

register_url = url + '/facebook/register/'

response = requests.post(
    register_url,
    data={
        'username': 'kekis',
        'password': 'python33'
    }
)

print(response.status_code)