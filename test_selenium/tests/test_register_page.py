import string
import random
import time

from test_selenium.tests.lib.constant_register_page import RegisterPage
from test_selenium.tests.lib.waitings import *


def test_page_register(browser):
    browser.get(url=browser.base_url + "/index.php?route=account/register")
    assert browser.title == RegisterPage.TITLE_REGISTER_PAGE


def test_check_coll_list_group(browser):
    coll_group = wait_of_elements(browser, RegisterPage.LIST_GROUP)
    assert len(coll_group) == 13


def random_string(num=1):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(num))
    return rand_string


def test_check_fields(browser):
    rand_str = random_string()
    wait_of_element(browser, RegisterPage.FIELD_FIRST_NAME).click()
    wait_of_element(browser, RegisterPage.FIELD_FIRST_NAME).send_keys(RegisterPage.FIRST_NAME + rand_str)
    wait_of_element(browser, RegisterPage.FIELD_LAST_NAME).click()
    wait_of_element(browser, RegisterPage.FIELD_LAST_NAME).send_keys(RegisterPage.LAST_NAME + rand_str)
    wait_of_element(browser, RegisterPage.FIELD_EMAIL).click()
    wait_of_element(browser, RegisterPage.FIELD_EMAIL).send_keys(RegisterPage.EMAIL + rand_str)
    wait_of_element(browser, RegisterPage.FIELD_TELEPHONE).click()
    wait_of_element(browser, RegisterPage.FIELD_TELEPHONE).send_keys(RegisterPage.TELEPHONE)

    wait_of_element(browser, RegisterPage.FIELD_PASSWORD).click()
    wait_of_element(browser, RegisterPage.FIELD_PASSWORD).send_keys(RegisterPage.PASSWORD)
    wait_of_element(browser, RegisterPage.FIELD_PASSWORD_CONFIRM).click()
    wait_of_element(browser, RegisterPage.FIELD_PASSWORD_CONFIRM).send_keys(RegisterPage.PASSWORD)

    wait_of_element(browser, RegisterPage.CHECKBOX_PRIVACY_POL).click()
    wait_of_element(browser, RegisterPage.BUTTON_CONTINUE).click()


def test_success(browser):
    assert browser.title == RegisterPage.TITLE_SUCCESS
