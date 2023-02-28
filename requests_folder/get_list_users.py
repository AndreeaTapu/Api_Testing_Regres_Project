import requests


def get_list_users(page=""):
    # response = ""
    if page == "":
        response = requests.get("https://reqres.in/api/users")
    else:
        response = requests.get(f"https://reqres.in/api/users?page={page}")
    return response
