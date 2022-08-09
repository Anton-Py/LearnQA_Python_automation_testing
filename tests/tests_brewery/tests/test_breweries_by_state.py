import json
import pytest
from jsonschema import validate
from tests.tests_brewery.lib.assertions import Assertions
from tests.tests_brewery.lib.constants import Constants
from tests.tests_brewery.lib.my_requests import MyRequests


@pytest.mark.parametrize("query, number", [("new_york", "3"), ("Idaho", "2"), ("alabama", "3")])
def test_get_breweries_by_state(base_url, query, number):
    data = {"by_state": f"{query}",
            "per_page": f"{number}"}
    response = MyRequests.get(base_url, data)
    # print(json.dumps(response.json(), indent=4))

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)
    Assertions.assert_json_value_by_name(response, "state", Constants.STATE_DICT[f"{query}"], "Wrong state")

    validate(instance=response.json(), schema=Constants.schema_for_breweries)
