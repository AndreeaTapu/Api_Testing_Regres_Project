from requests_folder.put_update_user import put_update_user


class TestPutUpdateUser:
    def test_put_update_user(self):
        response = put_update_user("morpheus", "zion resident")
        assert response.status_code == 200, f"Error: Status code is not valid. Expected 200, actual:{response.status_code}"
        assert response.json()["job"] == "zion resident", f"Error: Job is invalid. Expected: zion resident. Actual: {response.json()['job']}"
