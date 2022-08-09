import pytest
from jsonschema import validate
from tests.tests_jsonplaceholder.lib.assertions import Assertions
from tests.tests_jsonplaceholder.lib.constants import Constants
from tests.tests_jsonplaceholder.lib.my_requests import MyRequests


@pytest.mark.parametrize("number", [1, 2, 3, 4])
def test_delete_resource(base_url, number):
    url = base_url + "/posts/"f'{number}'
    data = {
        "title": "two",
        "body": "bar",
        "userId0": f'{number}'
    }
    response = MyRequests.delete(url, data)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE_GET)
    Assertions.assert_jsonplaceholde_delete(response, "id", f"{number}", "Wrong state")

    validate(instance=response.json(), schema=Constants.schema_for_jsonplaceholder_delete_resource)
