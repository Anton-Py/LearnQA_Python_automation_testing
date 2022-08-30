from tests_page_obgect.pages.CheckCurrencyPage import CheckCurrency
from tests_page_obgect.pages.MainPage import MainPage


def test_currency(driver):
    MainPage(driver).open()
    CheckCurrency(driver).get_text_from_button_header()
    CheckCurrency(driver).change_currency()
