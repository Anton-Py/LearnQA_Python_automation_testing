import time
from tests_allure.tests.lib.constant_delete_product_page import DeleteForProductPage
from tests_allure.pages.BasePage import BasePage


class DeleteProductPage(BasePage):

    def find_product(self):
        self.element_in_element(DeleteForProductPage.TABLE_STR, DeleteForProductPage.CHECKBOX).click()

    def add_delete(self):
        self._click(self.element(DeleteForProductPage.BUTTON_DELETE))
        time.sleep(5)
