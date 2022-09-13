from tests_allure.pages.BasePage import BasePage
from tests_allure.helpers import random_email, create_random_int, random_string
import string
import random

from tests_allure.tests.lib.constant_register_page import RegisterForPage


class RegisterPage(BasePage):
    path = "/index.php?route=account/register"

    def open(self):
        self.driver.get(self.base_url + self.path)

    def coll_groups_in_register_page(self):
        return self.coll_elements(RegisterForPage.LIST_GROUP)

    def registration(self):
        self._input(self.element(RegisterForPage.FIELD_FIRST_NAME), RegisterForPage.FIRST_NAME + random_string(1))
        self._input(self.element(RegisterForPage.FIELD_LAST_NAME), RegisterForPage.LAST_NAME + random_string(1))
        self._input(self.element(RegisterForPage.FIELD_EMAIL), random_email())
        self._input(self.element(RegisterForPage.FIELD_TELEPHONE), RegisterForPage.TELEPHONE + str(create_random_int()))
        self._input(self.element(RegisterForPage.FIELD_PASSWORD), RegisterForPage.PASSWORD)
        self._input(self.element(RegisterForPage.FIELD_PASSWORD_CONFIRM), RegisterForPage.PASSWORD)

    def click_checkbox_privacy_pol(self):
        self._click(self.element(RegisterForPage.CHECKBOX_PRIVACY_POL))

    def click_button_continue(self):
        self._click(self.element(RegisterForPage.BUTTON_CONTINUE))
