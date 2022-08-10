import pytest
from jsonschema import validate
from tests_api.tests_jsonplaceholder.lib.assertions import Assertions
from tests_api.tests_jsonplaceholder.lib.constants import Constants
from tests_api.tests_jsonplaceholder.lib.my_requests import MyRequests


@pytest.mark.parametrize("number", [2, 5, 3, 7])
def test_comments(base_url, number):
    url = base_url + "/posts/"f'{number}'"/comments"

    response = MyRequests.get(url)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE_GET)
    Assertions.assert_jsonplaceholde_comments(response, "postId", int(f"{number}"), "Wrong state")

    validate(instance=response.json(), schema=Constants.schema_for_jsonplaceholder_comments)
