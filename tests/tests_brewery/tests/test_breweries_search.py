import pytest
from jsonschema import validate
from tests.tests_brewery.lib.assertions import Assertions
from tests.tests_brewery.lib.constants import Constants
from tests.tests_brewery.lib.my_requests import MyRequests


@pytest.mark.parametrize("query", ["dog", "rog", "gor", "age"])
def test_get_breweries_search(base_url, query):
    url = base_url + "/search"
    data = {"query": f"{query}"}
    response = MyRequests.get(url, data)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)

    validate(instance=response.json(), schema=Constants.schema_for_breweries)
