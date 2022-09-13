from selenium.webdriver.common.by import By
from tests_allure.elements.test_data import get_currency
from tests_allure.pages.BasePage import BasePage
from tests_allure.tests.lib.constant_check_currency_page import CheckForCurrencyPage


class CheckCurrency(BasePage):

    def get_text_from_button_header(self):
        return self.element(CheckForCurrencyPage.BUTTON_CURRENCY).find_element(By.CSS_SELECTOR, 'button Strong').text

    def change_currency(self):
        self._click(self.element(CheckForCurrencyPage.BUTTON_CURRENCY))
        self._click(self.element(get_currency()))
        assert self.get_text_from_button_header() in self.element(CheckForCurrencyPage.SYMBOL_CURRENCY).text
