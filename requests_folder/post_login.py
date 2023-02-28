import requests


def post_login(email="", password=""):
    request_body = {
        "email": email,
        "password": password
    }
    response = requests.post("https://reqres.in/api/login", json=request_body)
    return response
