import pytest
from jsonschema import validate
from tests_api.tests_jsonplaceholder.lib.assertions import Assertions
from tests_api.tests_jsonplaceholder.lib.constants import Constants
from tests_api.tests_jsonplaceholder.lib.my_requests import MyRequests


@pytest.mark.parametrize("number", [2, 5, 3, 7])
def test_updating_resource(base_url, number):
    url = base_url + "/posts/"f'{number}'
    data = {
        "title": "two",
        "body": "bar",
        "userId0": f'{number}'
    }
    response = MyRequests.put(url, data)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE_GET)
    Assertions.assert_jsonplaceholde(response, "id", int(f"{number}"), "Wrong state")

    validate(instance=response.json(), schema=Constants.schema_for_jsonplaceholder_updating_resource)
