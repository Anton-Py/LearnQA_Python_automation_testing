import time
import random
from test_selenium.tests.lib.constant_card_product import CardProduct
from test_selenium.tests.lib.waitings import *


def test_main_page(driver):
    driver.get(url=driver.base_url)
    assert driver.title == CardProduct.TITLE_MAIN_PAGE


def test_tab_card_product(driver):
    # click card product
    wait_of_element_link(driver, CardProduct.PRODUCT_LINK).click()
    assert driver.title == CardProduct.TITLE_PRODUCT_PAGE


def test_check_cards_characteristics(driver):
    # check coll card img
    col_img = wait_of_elements(driver, CardProduct.CARD_CHARACTERISTICS)
    assert len(col_img) == 5


def test_check_buy_button(driver):
    # check but button
    wait_of_element(driver, CardProduct.BUY_BUTTON)


def test_check_field_quantity(driver):
    # check field
    wait_of_element(driver, CardProduct.FIELD_QUANTITITY)


def test_check_description_tabs(driver):
    wait_of_element_link(driver, CardProduct.DESCRIPTION_LINK).click()
    wait_of_element_link(driver, CardProduct.SPECIFICATION_LINK).click()
    wait_of_element_link(driver, CardProduct.REVIRWS_LINK).click()
