import requests


def delete_user():
    response = requests.delete("https://reqres.in/api/users/2")
    return response
