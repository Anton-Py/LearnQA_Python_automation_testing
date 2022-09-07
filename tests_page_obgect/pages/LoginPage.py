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

    def check_button_logout(self):
        self.check_element(LoginForPage.BUTTON_LOGOUT)

    def find_elements_menu(self):
        return self.elements_in_element(LoginForPage.ELEMENT_MENU, LoginForPage.ELEM_IN_MENU)

    def login(self):
        self._input(self.element(LoginForPage.FIELD_USERNAME), LoginForPage.USERNAME)
        self._input(self.element(LoginForPage.FIELD_PASSWORD), LoginForPage.PASSWORD)
        self._click(self.element(LoginForPage.BUTTON_LOGIN))
