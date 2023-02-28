from requests_folder.post_create_user import post_create_user


class TestCreateUser:
    def test_create_user(self):
        response = post_create_user("morpheus", "leader")
        assert response.status_code == 201, f"Error: Status code is not valid. Expected 201, actual:{response.status_code}"
        assert len(response.json()["id"]) > 0, f"Error: User id is invalid. Expected length greater than zero. Actual length: {len(response.json()['id'])} "
