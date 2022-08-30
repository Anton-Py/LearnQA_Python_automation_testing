import time
import random
from test_selenium.tests.lib.constant_catalog_page import CatalogPage
from test_selenium.tests.lib.waitings import *


def test_main_page(driver):
    driver.get(url=driver.base_url)
    assert driver.title == CatalogPage.TITLE_MAIN_PAGE


def test_tab_catalog(driver):
    # click tab catalog
    wait_of_element(driver, CatalogPage.TAB_MP3).click()
    wait_of_element(driver, CatalogPage.TAB_SEE_ALL).click()
    assert driver.title == CatalogPage.TITLE_CATALOG_PAGE


def test_coll_products(driver):
    product_elements = wait_of_elements(driver, CatalogPage.ELEM_PRODUCT)
    assert len(product_elements) == 4


def test_list_grop(driver):
    elements = wait_of_elements(driver, CatalogPage.COLL_GROUP_ELEMENTS)
    assert len(elements) == 26
    return elements


def test_check_switchdis_to_group(driver):
    elements = test_list_grop(driver)
    # for i in pages[7:]:
    #     print(i.get_attribute("textContent"))
    random_group = random.choice(elements[7:])
    text_random_group = random_group.get_attribute("textContent")
    random_group.click()
    group_elem = wait_of_element(driver, CatalogPage.GROUP_AFTER_CLICK)
    text_group_elem = group_elem.get_attribute("textContent")
    assert text_group_elem in text_random_group
