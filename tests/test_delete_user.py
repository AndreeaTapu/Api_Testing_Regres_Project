from requests_folder.delete_delete_user import delete_user


class TestDeleteUser:
    def test_delete_user(self):
        response = delete_user()
        assert response.status_code == 204, f"Error: Status code is not valid. Expected 201, actual:{response.status_code}"
