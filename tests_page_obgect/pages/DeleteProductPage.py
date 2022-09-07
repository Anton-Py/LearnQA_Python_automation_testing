import time
from tests_page_obgect.tests.lib.constant_delete_product_page import DeleteForProductPage
from tests_page_obgect.pages.BasePage import BasePage


class DeleteProductPage(BasePage):

    def find_product(self):
        self.element_in_element(DeleteForProductPage.TABLE_STR, DeleteForProductPage.CHECKBOX).click()

    def add_delete(self):
        self._click(self.element(DeleteForProductPage.BUTTON_DELETE))
        time.sleep(5)
