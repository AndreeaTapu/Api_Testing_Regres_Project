import requests


def get_list_resource():
    response = requests.get("https://reqres.in/api/unknown")
    return response
