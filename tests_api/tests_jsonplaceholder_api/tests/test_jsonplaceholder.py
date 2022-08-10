import pytest
from jsonschema import validate
from tests_api.tests_jsonplaceholder_api.lib.assertions import Assertions
from tests_api.tests_jsonplaceholder_api.lib.constants import Constants
from tests_api.tests_jsonplaceholder_api.lib.my_requests import MyRequests


@pytest.mark.parametrize("number", [2, 5, 3, 7])
def test_comments(base_url, number):
    url = base_url + "/posts/"f'{number}'"/comments"

    response = MyRequests.get(url)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE_GET)
    Assertions.assert_jsonplaceholde_comments(response, "postId", int(f"{number}"), "Wrong state")

    validate(instance=response.json(), schema=Constants.schema_for_jsonplaceholder_comments)


@pytest.mark.parametrize("number", [4, 3, 2, 5])
def test_creating_resource(base_url, number):
    url = base_url + "/posts"
    data = {
        "title": "two",
        "body": "bar",
        "userId0": f'{number}'
    }
    response = MyRequests.post(url, data)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE_POST)
    Assertions.assert_jsonplaceholde(response, "userId0", f"{number}", "Wrong state")

    validate(instance=response.json(), schema=Constants.schema_for_jsonplaceholder_creating_resource)


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


@pytest.mark.parametrize("number", [4, 3, 9, 5])
def test_getting_resource(base_url, number):
    url = base_url + "/posts/"f'{number}'
    data = {
        "title": "two",
        "body": "bar",
        "userId0": 2
    }
    response = MyRequests.get(url, data)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE_GET)
    Assertions.assert_jsonplaceholde(response, "id", int(f"{number}"), "Wrong state")

    validate(instance=response.json(), schema=Constants.schema_for_jsonplaceholder_getting_resource)


@pytest.mark.parametrize("number", [2, 5, 3, 7])
def test_updating_resource(base_url, number):
    url = base_url + "/posts/"f'{number}'
    data = {
        "title": "two",
        "body": "bar",
        "userId0": f'{number}'
    }
    response = MyRequests.put(url, data)

    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE_GET)
    Assertions.assert_jsonplaceholde(response, "id", int(f"{number}"), "Wrong state")

    validate(instance=response.json(), schema=Constants.schema_for_jsonplaceholder_updating_resource)
