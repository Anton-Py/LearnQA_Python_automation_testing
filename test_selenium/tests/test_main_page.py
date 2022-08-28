from test_selenium.tests.lib.constant_main_page import MainPage
from test_selenium.tests.lib.waitings import *


def test_main_page(driver):
    driver.get(url=driver.base_url)
    assert driver.title == MainPage.TITLE_MAIN_PAGE


def test_navbar(driver):
    # check navbar
    wait_of_element(driver, MainPage.GENERAL_ELEM_NAVBAR)
    navbar_tabs = wait_of_elements(driver, MainPage.ELEM_NAVBAR_FOR_CHOISE)
    assert len(navbar_tabs) == 8


def test_account(driver):
    # check links my account
    wait_of_element(driver, MainPage.BUTTON_ACCOUNT).click()
    wait_of_elements_link(driver, MainPage.LINK_REGISTER)
    wait_of_elements_link(driver, MainPage.LINK_LOGIN)


def test_coll_products(driver):
    # check products for page
    product_elements = wait_of_elements(driver, MainPage.ELEM_PRODUCT)
    assert len(product_elements) == 4


def test_search(driver):
    # check search
    wait_of_element(driver, MainPage.FIELD_SEARCH).click()
    wait_of_element(driver, MainPage.FIELD_SEARCH).send_keys("main")
    wait_of_element(driver, MainPage.BUTTON_SEARCH).click()
    assert driver.title == MainPage.TITLE_SEARCH_PAGE
    wait_of_element(driver, MainPage.CHECKBOX_DESCRIPTION).click()
    wait_of_element(driver, MainPage.BLUE_BUTTON_SEARCH).click()
    elements = wait_of_elements(driver, MainPage.ELEM_PRODUCT_SEARCH, time=3)
    assert len(elements) > 0
