import time
import random
from test_selenium.tests.lib.constant_card_product import CardProduct
from test_selenium.tests.lib.waitings import *


def test_main_page(browser):
    browser.get(url=browser.base_url)
    assert browser.title == CardProduct.TITLE_MAIN_PAGE


def test_tab_card_product(browser):
    # click card product
    wait_of_element_link(browser, CardProduct.PRODUCT_LINK).click()
    assert browser.title == CardProduct.TITLE_PRODUCT_PAGE


def test_check_cards_characteristics(browser):
    # check coll card img
    col_img = wait_of_elements(browser, CardProduct.CARD_CHARACTERISTICS)
    assert len(col_img) == 5


def test_check_buy_button(browser):
    # check but button
    wait_of_element(browser, CardProduct.BUY_BUTTON)


def test_check_field_quantity(browser):
    # check field
    wait_of_element(browser, CardProduct.FIELD_QUANTITITY)


def test_check_description_tabs(browser):
    wait_of_element_link(browser, CardProduct.DESCRIPTION_LINK).click()
    wait_of_element_link(browser, CardProduct.SPECIFICATION_LINK).click()
    wait_of_element_link(browser, CardProduct.REVIRWS_LINK).click()
