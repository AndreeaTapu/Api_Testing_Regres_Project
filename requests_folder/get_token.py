import requests
import random


def generate_token():
    nr = random.randint(1, 99999999999999999999)
    request_body = {
        "email": f"eve.holt{nr}@reqres.in",
        "password": "pistol"
    }
    response = requests.post("https://reqres.in/api/register", json=request_body)
    token = response.json()["token"]
    return token
