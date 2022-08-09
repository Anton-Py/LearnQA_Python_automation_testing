import requests
from tests.tests_two_params.lib.assertions import Assertions
from tests.tests_two_params.lib.my_requests import MyRequests


def test_two_params(base_url, status_code):
    HEADERS = {"API-Key": "9c49f6e42ceae6da88a692c08d634199",
               "User-Agent": "Mozilla/5.0 (X11; Linux x86) AppleWebKit/537.36 (KHTML, like Gecko Chrome/62.0.3202.75 "
                             "Safari/537.36/TEST"}
    response = MyRequests.get(base_url, headers=HEADERS)
    Assertions.assert_code_status(response, int(status_code))
