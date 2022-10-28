from test_selenium.tests.lib.constant_main_page import MainPage
from test_selenium.tests.lib.waitings import *


def test_main_page(browser):
    browser.get(url=browser.base_url)
    assert browser.title == MainPage.TITLE_MAIN_PAGE


def test_navbar(browser):
    # check navbar
    wait_of_element(browser, MainPage.GENERAL_ELEM_NAVBAR)
    navbar_tabs = wait_of_elements(browser, MainPage.ELEM_NAVBAR_FOR_CHOISE)
    assert len(navbar_tabs) == 8


def test_account(browser):
    # check links my account
    wait_of_element(browser, MainPage.BUTTON_ACCOUNT).click()
    wait_of_elements_link(browser, MainPage.LINK_REGISTER)
    wait_of_elements_link(browser, MainPage.LINK_LOGIN)


def test_coll_products(browser):
    # check products for page
    product_elements = wait_of_elements(browser, MainPage.ELEM_PRODUCT)
    assert len(product_elements) == 4


def test_search(browser):
    # check search
    wait_of_element(browser, MainPage.FIELD_SEARCH).click()
    wait_of_element(browser, MainPage.FIELD_SEARCH).send_keys("main")
    wait_of_element(browser, MainPage.BUTTON_SEARCH).click()
    assert browser.title == MainPage.TITLE_SEARCH_PAGE
    wait_of_element(browser, MainPage.CHECKBOX_DESCRIPTION).click()
    wait_of_element(browser, MainPage.BLUE_BUTTON_SEARCH).click()
    elements = wait_of_elements(browser, MainPage.ELEM_PRODUCT_SEARCH, time=3)
    assert len(elements) > 0
