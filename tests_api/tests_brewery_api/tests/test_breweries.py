import pytest
from jsonschema import validate
from tests_api.tests_brewery_api.lib.assertions import Assertions
from tests_api.tests_brewery_api.lib.constants import Constants
from tests_api.tests_brewery_api.lib.my_requests import MyRequests


@pytest.mark.parametrize("query, number",
                         [("san_diego", "3"), ("new_york", "4"), ("chicago", "5"), ("washington", "4")])
def test_get_breweries_by_city(base_url, query, number):
    data = {"by_city": f"{query}",
            "per_page": f"{number}"}
    response = MyRequests.get(base_url, data)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)
    Assertions.assert_json_value_by_name(response, "city", Constants.CITY_DICT[f"{query}"], "Wrong city")

    validate(instance=response.json(), schema=Constants.schema_for_breweries)


@pytest.mark.parametrize("query, number", [("new_york", "3"), ("Idaho", "2"), ("alabama", "3")])
def test_get_breweries_by_state(base_url, query, number):
    data = {"by_state": f"{query}",
            "per_page": f"{number}"}
    response = MyRequests.get(base_url, data)
    # print(json.dumps(response.json(), indent=4))

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)
    Assertions.assert_json_value_by_name(response, "state", Constants.STATE_DICT[f"{query}"], "Wrong state")

    validate(instance=response.json(), schema=Constants.schema_for_breweries)


@pytest.mark.parametrize("query, number", [("closed", "2"), ("bar", "3"), ("large", "3"), ("nano", "2")])
def test_get_breweries_by_type(base_url, query, number):
    data = {"by_type": f"{query}",
            "per_page": f"{number}"}
    response = MyRequests.get(base_url, data)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)
    Assertions.assert_json_value_by_name(response, "brewery_type", Constants.TYPE_DICT[f"{query}"], "Wrong type")

    validate(instance=response.json(), schema=Constants.schema_for_breweries)


def test_get_breweries_random(base_url):
    url = base_url + "/random"
    response = MyRequests.get(url)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)

    validate(instance=response.json(), schema=Constants.schema_for_breweries)


@pytest.mark.parametrize("query", ["dog", "rog", "gor", "age"])
def test_get_breweries_search(base_url, query):
    url = base_url + "/search"
    data = {"query": f"{query}"}
    response = MyRequests.get(url, data)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)

    validate(instance=response.json(), schema=Constants.schema_for_breweries)
