import time
from test_selenium.tests.lib.constant_login_page import LoginPage
from test_selenium.tests.lib.waitings import *


def test_page_admin(driver):
    driver.get(url=driver.base_url + "/admin")
    assert driver.title == LoginPage.TITLE_LOGIN_PAGE


def test_check_coll_field(driver):
    coll_field = wait_of_elements(driver, LoginPage.SELECTOR_FIELD)
    assert len(coll_field) == 2


def test_forgotten_password(driver):
    # check link elem
    wait_of_element(driver, LoginPage.FORGOTTEN_LINK)


def test_past_login_password(driver):
    wait_of_element(driver, LoginPage.FIELD_USERNAME).click()
    wait_of_element(driver, LoginPage.FIELD_USERNAME).send_keys(LoginPage.USERNAME)
    wait_of_element(driver, LoginPage.FIELD_PASSWORD).click()
    wait_of_element(driver, LoginPage.FIELD_PASSWORD).send_keys(LoginPage.PASSWORD)
    wait_of_element(driver, LoginPage.BUTTON_LOGIN).click()


def test_success(driver):
    assert driver.title == LoginPage.TITLE_SUCCESS
