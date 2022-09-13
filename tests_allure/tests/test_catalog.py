import time
import random
from tests_allure.pages.CatalogPage import CatalogPage
from tests_allure.tests.lib.constant_catalog_page import CatalogForPage


def test_main_page(browser):
    page = CatalogPage(browser)
    page.open()
    assert browser.title == CatalogForPage.TITLE_MAIN_PAGE
    page.click_catalog_tab_mp3()
    page.click_catalog_tab_see_all()
    assert browser.title == CatalogForPage.TITLE_CATALOG_PAGE
    assert len(page.coll_products()) == 4
    assert len(page.list_group()) == 26
    random_group = page.randoming(page.list_group()[7:])
    text_random_group = page.get_text(random_group)
    page._click(random_group)
    text_group_elem = page.get_text(page.elem())
    assert text_group_elem in text_random_group
