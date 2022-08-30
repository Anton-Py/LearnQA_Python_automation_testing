import time
import random
from tests_page_obgect.pages.CatalogPage import CatalogPage
from tests_page_obgect.tests.lib.constant_catalog_page import CatalogForPage


def test_main_page(driver):
    CatalogPage(driver).open()
    assert driver.title == CatalogForPage.TITLE_MAIN_PAGE
    CatalogPage(driver).click_catalog_tab_mp3()
    CatalogPage(driver).click_catalog_tab_see_all()
    assert driver.title == CatalogForPage.TITLE_CATALOG_PAGE
    assert len(CatalogPage(driver).coll_products()) == 4
    assert len(CatalogPage(driver).list_group()) == 26
    random_group = CatalogPage(driver).randoming(CatalogPage(driver).list_group()[7:])
    text_random_group = CatalogPage(driver).get_text(random_group)
    CatalogPage(driver)._click(random_group)
    text_group_elem = CatalogPage(driver).get_text(CatalogPage(driver).elem())
    assert text_group_elem in text_random_group
