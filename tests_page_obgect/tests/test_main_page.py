from tests_page_obgect.pages.MainPage import *


def test_main_page(driver):
    MainPage(driver).open()
    assert driver.title == MainForPage.TITLE_MAIN_PAGE
    MainPage(driver).check_element_navbar()
    assert len(MainPage(driver).check_elements_navbar_tabs()) == 8
    MainPage(driver).click_button()
    MainPage(driver).check_link_register()
    MainPage(driver).check_link_login()
    MainPage(driver).check_coll_products()
    assert len(MainPage(driver).check_coll_products()) == 4
    MainPage(driver).check_input_search()
    MainPage(driver).click_button_search()
    assert driver.title == MainForPage.TITLE_SEARCH_PAGE
    MainPage(driver).click_checkbox()
    MainPage(driver).click_blue_button_search()
    assert len(MainPage(driver).elem_product_search()) > 0
