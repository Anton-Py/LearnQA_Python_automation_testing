import random
from tests_allure.tests.lib.constant_catalog_page import CatalogForPage
from tests_allure.pages.BasePage import BasePage


class CatalogPage(BasePage):

    def open(self):
        self.driver.get(self.base_url)

    def click_catalog_tab_mp3(self):
        self._click(self.element(CatalogForPage.TAB_MP3))

    def click_catalog_tab_see_all(self):
        self._click(self.element(CatalogForPage.TAB_SEE_ALL))

    def coll_products(self):
        return self.elements(CatalogForPage.ELEM_PRODUCT)

    def list_group(self):
        return self.elements(CatalogForPage.COLL_GROUP_ELEMENTS)

    def elem(self):
        return self.element(CatalogForPage.GROUP_AFTER_CLICK)

    def randoming(self, elements):
        element = random.choice(elements)
        return element

    def get_text(self, element):
        text = element.get_attribute("textContent")
        return text
