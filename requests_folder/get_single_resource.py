import requests


def get_single_resource():
    response = requests.get("https://reqres.in/api/unknown/2")
    return response


def get_single_resource_not_found():
    response = requests.get("https://reqres.in/api/unknown/3")
    return response
