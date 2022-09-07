from tests_page_obgect.pages.RegisterPage import *


def test_page_register(driver):
    RegisterPage(driver).open()
    assert driver.title == RegisterForPage.TITLE_REGISTER_PAGE
    assert len(RegisterPage(driver).coll_groups_in_register_page()) == 13
    RegisterPage(driver).registration()
    RegisterPage(driver).click_checkbox_privacy_pol()
    RegisterPage(driver).click_button_continue()
    assert driver.title == RegisterForPage.TITLE_SUCCESS
