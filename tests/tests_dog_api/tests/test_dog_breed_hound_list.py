from jsonschema import validate
from tests.tests_dog_api.lib.assertions import Assertions
from tests.tests_dog_api.lib.constants import Constants
from tests.tests_dog_api.lib.my_requests import MyRequests


def test_get_bred_hound_list(base_url):
    url = base_url + "/breed/hound/list"
    response = MyRequests.get(url)
    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)

    validate(instance=response.json(), schema=Constants.schema_for_bred_hound_list)
