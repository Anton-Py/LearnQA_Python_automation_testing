import pytest
import random
from jsonschema import validate
from tests.tests_dog_api.lib.assertions import Assertions
from tests.tests_dog_api.lib.constants import Constants
from tests.tests_dog_api.lib.my_requests import MyRequests


def get_list_all_breeds(base_url):
    url = base_url + "/breeds/list/all"
    response = MyRequests.get(url)
    Assertions.assert_code_status(response, Constants.EXPECTED_STATUS_CODE)
    bread = random.choice(list(response.json()["message"]))
    # bread = list(response.json()["message"])    # как передать список собак из этой функи в фикстуру параметризации?
    return bread


def test_get_specific_breed_images_random(base_url):
    url = base_url + f"/breed/{get_list_all_breeds(base_url)}/images/random"
    response = MyRequests.get(url)

    validate(instance=response.json(), schema=Constants.schema_for_specific_breed_images_random)


@pytest.mark.parametrize("bread", ["affenpinscher", "australian", "borzoi", "bulldog", "chihuahua", "entlebucher"])
def test_get_specific_breed_images_random_params(base_url, bread):
    url = base_url + f"/breed/{bread}/images/random"
    response = MyRequests.get(url)

    validate(instance=response.json(), schema=Constants.schema_for_specific_breed_images_random)
