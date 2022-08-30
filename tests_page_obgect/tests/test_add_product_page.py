from tests_page_obgect.elements.AlertElement import AlertElement
from tests_page_obgect.tests.lib.constant_add_product_page import AddForProductPage
from tests_page_obgect.pages.AddProductPage import AddProductPage
from tests_page_obgect.pages.LoginPage import LoginPage


def test_login_page(driver):
    AddProductPage(driver).open()
    assert driver.title == AddForProductPage.TITLE_LOGIN_PAGE
    LoginPage(driver).login()
    AddProductPage(driver).click_catalog()
    AddProductPage(driver).select_tab_product()
    AddProductPage(driver).click_button_plus()
    AddProductPage(driver).creating_card()
    AlertElement(driver).popup_alert()
