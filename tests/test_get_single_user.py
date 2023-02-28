from requests_folder.get_single_user import get_single_user


class TestGetSingleUser:
    def test_get_single_user(self):
        response = get_single_user()
        assert response.status_code, f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"

    def test_get_single_user_not_found(self):
        response = get_single_user()
        assert response.status_code, f"Error: status code is not correct. Expected: 404, Actual: {response.status_code}"
