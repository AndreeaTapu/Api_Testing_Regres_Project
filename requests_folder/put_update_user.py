import requests


def put_update_user(name, job):
    request_body = {
        "name": name,
        "job": job
    }
    response = requests.put("https://reqres.in/api/users/2", json=request_body)
    return response
