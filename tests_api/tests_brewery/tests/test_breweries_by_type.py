import pytest
from jsonschema import validate
from tests_api.tests_brewery.lib.assertions import Assertions
from tests_api.tests_brewery.lib.constants import Constants
from tests_api.tests_brewery.lib.my_requests import MyRequests


@pytest.mark.parametrize("query, number", [("closed", "2"), ("bar", "3"), ("large", "3"), ("nano", "2")])
def test_get_breweries_by_type(base_url, query, number):
    data = {"by_type": f"{query}",
            "per_page": f"{number}"}
    response = MyRequests.get(base_url, data)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)
    Assertions.assert_json_value_by_name(response, "brewery_type", Constants.TYPE_DICT[f"{query}"], "Wrong type")

    validate(instance=response.json(), schema=Constants.schema_for_breweries)
