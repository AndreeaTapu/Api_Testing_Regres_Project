from requests_folder.get_list_users import get_list_users


class TestGetListUsers:
    def test_get_list_users_no_filter_check_response_status(self):
        response = get_list_users()
        assert response.status_code, f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert len(response.json()) == 6, f"Expected: 6, actual: {len(response.json())}"
        assert response.json()["page"] == 1, f"Expected page: 1, actual: {response.json()['page']}"

    def test_get_list_users_filter_by_page_2(self):
        response = get_list_users(2).json()
        assert response["page"] == 2, f"Expected page: 2, actual: {response['page']}"
        assert len(response) == 6, f"Expected: 6, actual: {len(response)}"
        assert response["per_page"] == 6, f"Expected per page: 6, actual: {response['per_page']}"
        assert len(response["data"]) == 6, f"Expected users: 6, actual: {len(response['data'])}"
