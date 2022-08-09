import pytest
from jsonschema import validate
from tests.tests_jsonplaceholder.lib.assertions import Assertions
from tests.tests_jsonplaceholder.lib.constants import Constants
from tests.tests_jsonplaceholder.lib.my_requests import MyRequests


@pytest.mark.parametrize("number", [4, 3, 2, 5])
def test_creating_resource(base_url, number):
    url = base_url + "/posts"
    data = {
        "title": "two",
        "body": "bar",
        "userId0": f'{number}'
    }
    response = MyRequests.post(url, data)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE_POST)
    Assertions.assert_jsonplaceholde(response, "userId0", f"{number}", "Wrong state")

    validate(instance=response.json(), schema=Constants.schema_for_jsonplaceholder_creating_resource)
