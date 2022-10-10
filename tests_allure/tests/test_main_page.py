from tests_allure.pages.MainPage import *
import pytest
import allure


@allure.title('Checking the main page')
@pytest.mark.parametrize('coll_elements_navbar_tabs', [8, 9], ids=['Истина', 'Ложь'])
def test_main_page(browser, coll_elements_navbar_tabs):
    page = MainPage(browser)
    page.open()
    assert browser.title == MainForPage.TITLE_MAIN_PAGE
    page.check_element_navbar()
    assert len(page.check_elements_navbar_tabs()) == 8
    page.click_button()
    page.check_link_register()
    page.check_link_login()
    page.check_coll_products()
    assert len(page.check_coll_products()) == 4
    page.check_input_search()
    page.click_button_search()
    assert browser.title == MainForPage.TITLE_SEARCH_PAGE
    page.click_checkbox()
    page.click_blue_button_search()
    assert len(page.elem_product_search()) > 0
