from requests_folder.post_login import post_login


class TestLoginUser:
    def test_login_successful(self):
        response = post_login("eve.holt@reqres.in", "cityslicka")
        assert response.status_code == 200, f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"

    def test_login_unsuccessful_missing_password(self):
        response = post_login("peter@klaven")
        assert response.status_code == 400, f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert response.json()["error"] == "Missing password", f"Error: incorrect error message. Expected: Missing password. Actual: {response.json()['error']}"

    def test_login_unsuccessful_user_not_found(self):
        response = post_login("eve.holt78@reqres.in", "cityslicka")
        assert response.status_code == 400, f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert response.json()["error"] == "user not found", f"Error: incorrect error message. Expected: Missing password. Actual: {response.json()['error']}"
