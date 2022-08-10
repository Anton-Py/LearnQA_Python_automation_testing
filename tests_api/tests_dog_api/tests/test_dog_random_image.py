import pytest
from jsonschema import validate
from tests_api.tests_dog_api.lib.assertions import Assertions
from tests_api.tests_dog_api.lib.constants import Constants
from tests_api.tests_dog_api.lib.my_requests import MyRequests


@pytest.mark.parametrize("number", [2, 5, 6, 4])
def test_get_list_all_breeds(base_url, number):
    url = base_url + f"/breeds/image/random/{number}"
    response = MyRequests.get(url)
    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)

    validate(instance=response.json(), schema=Constants.schema_for_dog_random_image)
