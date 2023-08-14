import requests

url = 'http://127.0.0.1:8000/'

list_url = url + 'todo/list/'
add_url = url + 'todo/add/'
complete_url = url + 'todo/complete/'


def task_client():
    # Cerem lista de taskuri
    response = requests.get(list_url)
    print(response.status_code)
    if response.status_code == 200:
        for a in response.json():
            print(a)
    add = input('add? y/n')
    if add == 'y':
        title = input('title')
        # Trimitem requiest la API pentru a crea
        response = requests.post(add_url, data={
            'title': title
        })
        print("Status", response.status_code)
        print("Content", response.content)

    add = input('complete? y/n')
    if add == 'y':
        id = input('id')
        # Trimitem requiest la API pentru a crea
        response = requests.post(complete_url, data={
            'id': int(id)
        })
        print("Status", response.status_code)
        print("Content", response.content)


while True:
    task_client()
