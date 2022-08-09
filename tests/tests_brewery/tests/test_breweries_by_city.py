import pytest
from jsonschema import validate
from tests.tests_brewery.lib.assertions import Assertions
from tests.tests_brewery.lib.constants import Constants
from tests.tests_brewery.lib.my_requests import MyRequests


@pytest.mark.parametrize("query, number",
                         [("san_diego", "3"), ("new_york", "4"), ("chicago", "5"), ("washington", "4")])
def test_get_breweries_by_city(base_url, query, number):
    data = {"by_city": f"{query}",
            "per_page": f"{number}"}
    response = MyRequests.get(base_url, data)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)
    Assertions.assert_json_value_by_name(response, "city", Constants.CITY_DICT[f"{query}"], "Wrong city")

    validate(instance=response.json(), schema=Constants.schema_for_breweries)
