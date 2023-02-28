from requests_folder.patch_update_user import patch_update_user


class TestPatchUpdateUser:
    def test_patch_update_user(self):
        response = patch_update_user("morpheus", "zion resident")
        assert response.status_code == 200, f"Error: Status code is not valid. Expected 200, actual:{response.status_code}"
        assert response.json()["job"] == "zion resident", f"Error: Job is invalid. Expected job is zion resident. Actual length: {response.json()['job']}"
