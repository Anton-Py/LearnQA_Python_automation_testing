from tests_page_obgect.tests.lib.constant_card_product import CardForProduct
from tests_page_obgect.pages.BasePage import BasePage


class CardProduct(BasePage):

    def open(self):
        self.driver.get(self.base_url)

    def check_element_button(self):
        self.check_element(CardForProduct.BUY_BUTTON)

    def check_element_field(self):
        self.check_element(CardForProduct.FIELD_QUANTITITY)

    def click_card_product_product_link(self):
        self._click(self.element(CardForProduct.PRODUCT_LINK))

    def click_card_product_description(self):
        self._click(self.element(CardForProduct.DESCRIPTION_LINK))

    def click_card_product_specification(self):
        self._click(self.element(CardForProduct.SPECIFICATION_LINK))

    def click_card_product_revirws(self):
        self._click(self.element(CardForProduct.REVIRWS_LINK))

    def coll(self):
        return self.elements(CardForProduct.CARD_CHARACTERISTICS)
