import requests


def get_single_user():
    response = requests.get("https://reqres.in/api/users/2")
    return response


def get_single_user_not_found():
    response = requests.get("https://reqres.in/api/users/23")
    return response
