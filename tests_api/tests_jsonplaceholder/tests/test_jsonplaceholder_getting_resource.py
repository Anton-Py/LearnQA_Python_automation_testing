import pytest
from jsonschema import validate
from tests_api.tests_jsonplaceholder.lib.assertions import Assertions
from tests_api.tests_jsonplaceholder.lib.constants import Constants
from tests_api.tests_jsonplaceholder.lib.my_requests import MyRequests


@pytest.mark.parametrize("number", [4, 3, 9, 5])
def test_getting_resource(base_url, number):
    url = base_url + "/posts/"f'{number}'
    data = {
        "title": "two",
        "body": "bar",
        "userId0": 2
    }
    response = MyRequests.get(url, data)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE_GET)
    Assertions.assert_jsonplaceholde(response, "id", int(f"{number}"), "Wrong state")

    validate(instance=response.json(), schema=Constants.schema_for_jsonplaceholder_getting_resource)
