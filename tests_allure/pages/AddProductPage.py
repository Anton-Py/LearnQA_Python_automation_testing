from tests_allure.tests.lib.constant_add_product_page import AddForProductPage
from tests_allure.pages.BasePage import BasePage


class AddProductPage(BasePage):
    path = "/admin"

    def open(self):
        self.driver.get(self.base_url + self.path)

    def click_catalog(self):
        self._click(self.element(AddForProductPage.MENU_CATALOG))

    def select_tab_product(self):
        self._click(self.element(AddForProductPage.ELEMENT_PRODUCT))

    def click_button_plus(self):
        self._click(self.element(AddForProductPage.BUTTON_PLUS))

    def creating_card(self):
        self._input(self.element(AddForProductPage.FIELD_NAME), AddForProductPage.NAME_PRODUCT)
        self._input(self.element(AddForProductPage.FIELD_DESCRIPTION), AddForProductPage.DESCRIPTION_PRODUCT)
        self._input(self.element(AddForProductPage.FIELD_META), AddForProductPage.META_PRODUCT)
        self._click(self.element(AddForProductPage.NAVBAR))
        self._input(self.element(AddForProductPage.FIELD_MODEL), AddForProductPage.MODEL_PRODUCT)
        self._input(self.element(AddForProductPage.FIELD_PRICE), AddForProductPage.PRICE_PRODUCT)
        self._click(self.element(AddForProductPage.BUTTON_SAVE))
