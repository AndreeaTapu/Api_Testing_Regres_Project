from requests_folder.get_single_resource import get_single_resource


class TestGetSingleResource:
    def test_get_single_resource(self):
        response = get_single_resource()
        assert response.status_code, f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"

    def test_get_single_resource_not_found(self):
        response = get_single_resource()
        assert response.status_code, f"Error: status code is not correct. Expected: 404, Actual: {response.status_code}"
