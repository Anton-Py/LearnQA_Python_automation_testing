from tests_allure.pages.CheckCurrencyPage import CheckCurrency
from tests_allure.pages.MainPage import MainPage


def test_currency(browser):
    page_check = CheckCurrency(browser)
    page_mane = MainPage(browser)
    page_mane.open()
    page_check.get_text_from_button_header()
    page_check.change_currency()
