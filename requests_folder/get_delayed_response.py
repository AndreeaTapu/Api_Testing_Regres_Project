import requests


def get_delayed_response():
    response = requests.put("https://reqres.in/api/users?delay = 3")
    return response
