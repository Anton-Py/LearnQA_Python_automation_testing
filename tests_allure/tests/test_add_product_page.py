from tests_allure.elements.AlertElement import AlertElement
from tests_allure.tests.lib.constant_add_product_page import AddForProductPage
from tests_allure.pages.AddProductPage import AddProductPage
from tests_allure.pages.LoginPage import LoginPage
import pytest
import allure


@allure.title('Authorization with wrong password')
def test_login_page(browser):
    page = AddProductPage(browser)
    page.open()
    assert browser.title == AddForProductPage.TITLE_LOGIN_PAGE
    LoginPage(browser).login()
    page.click_catalog()
    page.select_tab_product()
    page.click_button_plus()
    page.creating_card()
    AlertElement(browser).popup_alert()
