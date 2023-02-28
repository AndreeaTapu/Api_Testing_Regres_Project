from requests_folder.get_delayed_response import get_delayed_response


class TestGetDelayedResponse:
    def test_get_delayed_response(self):
        response = get_delayed_response()
        assert response.status_code, f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
