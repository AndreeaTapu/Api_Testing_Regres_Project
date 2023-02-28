from requests_folder.get_list_resource import get_list_resource


class TestGetListResource:
    def test_get_list_resource(self):
        response = get_list_resource()
        assert response.status_code, f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
