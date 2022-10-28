import time
from test_selenium.tests.lib.constant_login_page import LoginPage
from test_selenium.tests.lib.waitings import *


def test_page_admin(browser):
    browser.get(url=browser.base_url + "/admin")
    assert browser.title == LoginPage.TITLE_LOGIN_PAGE


def test_check_coll_field(browser):
    coll_field = wait_of_elements(browser, LoginPage.SELECTOR_FIELD)
    assert len(coll_field) == 2


def test_forgotten_password(browser):
    # check link elem
    wait_of_element(browser, LoginPage.FORGOTTEN_LINK)


def test_past_login_password(browser):
    wait_of_element(browser, LoginPage.FIELD_USERNAME).click()
    wait_of_element(browser, LoginPage.FIELD_USERNAME).send_keys(LoginPage.USERNAME)
    wait_of_element(browser, LoginPage.FIELD_PASSWORD).click()
    wait_of_element(browser, LoginPage.FIELD_PASSWORD).send_keys(LoginPage.PASSWORD)
    wait_of_element(browser, LoginPage.BUTTON_LOGIN).click()


def test_success(browser):
    assert browser.title == LoginPage.TITLE_SUCCESS
