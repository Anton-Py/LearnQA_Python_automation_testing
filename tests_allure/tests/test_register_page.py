from tests_allure.pages.RegisterPage import *


def test_page_register(browser):
    page = RegisterPage(browser)
    page.open()
    assert browser.title == RegisterForPage.TITLE_REGISTER_PAGE
    assert len(page.coll_groups_in_register_page()) == 13
    page.registration()
    page.click_checkbox_privacy_pol()
    page.click_button_continue()
    assert browser.title == RegisterForPage.TITLE_SUCCESS
