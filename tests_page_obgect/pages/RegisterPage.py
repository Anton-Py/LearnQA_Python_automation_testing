from tests_page_obgect.pages.BasePage import BasePage
from tests_page_obgect.helpers import random_email
import string
import random

from tests_page_obgect.tests.lib.constant_register_page import RegisterForPage


class RegisterPage(BasePage):
    path = "/index.php?route=account/register"

    def open(self):
        self.driver.get(self.base_url + self.path)

    def random_string(self, num=1):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(num))
        return rand_string

    def random_num(self):
        num = random.randint(10, 99)
        return num

    def coll_groups_in_register_page(self):
        return self.coll_elements(RegisterForPage.LIST_GROUP)

    def registration(self):
        self._input(self.element(RegisterForPage.FIELD_FIRST_NAME), RegisterForPage.FIRST_NAME + self.random_string())
        self._input(self.element(RegisterForPage.FIELD_LAST_NAME), RegisterForPage.LAST_NAME + self.random_string())
        self._input(self.element(RegisterForPage.FIELD_EMAIL), random_email())
        self._input(self.element(RegisterForPage.FIELD_TELEPHONE), RegisterForPage.TELEPHONE + str(self.random_num()))
        self._input(self.element(RegisterForPage.FIELD_PASSWORD), RegisterForPage.PASSWORD)
        self._input(self.element(RegisterForPage.FIELD_PASSWORD_CONFIRM), RegisterForPage.PASSWORD)

    def click_checkbox_privacy_pol(self):
        self._click(self.element(RegisterForPage.CHECKBOX_PRIVACY_POL))

    def click_button_continue(self):
        self._click(self.element(RegisterForPage.BUTTON_CONTINUE))
