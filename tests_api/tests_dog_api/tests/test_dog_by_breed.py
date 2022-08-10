from jsonschema import validate
from tests_api.tests_dog_api.lib.assertions import Assertions
from tests_api.tests_dog_api.lib.constants import Constants
from tests_api.tests_dog_api.lib.my_requests import MyRequests


def test_get_list_all_breed(base_url):
    url = base_url + "/breed/hound/images"
    response = MyRequests.get(url)
    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)

    validate(instance=response.json(), schema=Constants.schema_for_dog_by_breed)
