from tests_allure.tests.lib.constant_main_page import MainForPage
from tests_allure.pages.BasePage import BasePage


class MainPage(BasePage):

    def open(self):
        self.driver.get(self.base_url)

    def check_element_navbar(self):
        self.check_element(MainForPage.GENERAL_ELEM_NAVBAR)

    def check_elements_navbar_tabs(self):
        return self.coll_elements(MainForPage.ELEM_NAVBAR_FOR_CHOISE)

    def click_button(self):
        self._click(self.element(MainForPage.BUTTON_ACCOUNT))

    def check_link_register(self):
        self.check_element(MainForPage.LINK_REGISTER)

    def check_link_login(self):
        self.check_element(MainForPage.LINK_LOGIN)

    def check_coll_products(self):
        return self.coll_elements(MainForPage.ELEM_PRODUCT)

    def check_input_search(self):
        self._input(self.element(MainForPage.FIELD_SEARCH), MainForPage.VALUE_SEARCH)

    def click_button_search(self):
        self._click(self.element(MainForPage.BUTTON_SEARCH))

    def click_checkbox(self):
        self._click(self.element(MainForPage.CHECKBOX_DESCRIPTION))

    def click_blue_button_search(self):
        self._click(self.element(MainForPage.BLUE_BUTTON_SEARCH))

    def elem_product_search(self):
        return self.coll_elements(MainForPage.ELEM_PRODUCT_SEARCH)
