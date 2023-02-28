import requests


def post_create_user(name, job):
    request_body = {
        "name": name,
        "job": job
    }
    response = requests.post("https://reqres.in/api/users", json=request_body)
    return response
