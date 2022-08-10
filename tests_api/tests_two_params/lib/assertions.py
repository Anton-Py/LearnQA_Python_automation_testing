from requests import Response


class Assertions:

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expeted: {expected_status_code}. Actual: {response.status_code}"
