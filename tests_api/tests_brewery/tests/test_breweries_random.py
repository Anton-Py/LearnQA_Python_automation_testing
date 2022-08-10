from jsonschema import validate
from tests_api.tests_brewery.lib.assertions import Assertions
from tests_api.tests_brewery.lib.constants import Constants
from tests_api.tests_brewery.lib.my_requests import MyRequests


def test_get_breweries_random(base_url):
    url = base_url + "/random"
    response = MyRequests.get(url)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)

    validate(instance=response.json(), schema=Constants.schema_for_breweries)
