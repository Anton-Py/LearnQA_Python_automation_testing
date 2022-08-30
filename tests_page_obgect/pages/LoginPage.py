from tests_page_obgect.tests.lib.constant_login_page import LoginForPage
from tests_page_obgect.pages.BasePage import BasePage


class LoginPage(BasePage):
    path = "/admin"

    def open(self):
        self.driver.get(self.base_url + self.path)

    def coll(self):
        return self.coll_elements(LoginForPage.SELECTOR_FIELD)

    def check_element_password(self):
        self.check_element(LoginForPage.FORGOTTEN_LINK)

    def login(self):
        self._input(self.element(LoginForPage.FIELD_USERNAME), LoginForPage.USERNAME)
        self._input(self.element(LoginForPage.FIELD_PASSWORD), LoginForPage.PASSWORD)
        self._click(self.element(LoginForPage.BUTTON_LOGIN))
