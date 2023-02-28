import requests


def patch_update_user(name, job):
    request_body = {
        "name": name,
        "job": job
    }
    response = requests.patch("https://reqres.in/api/users/2", json=request_body)
    return response
