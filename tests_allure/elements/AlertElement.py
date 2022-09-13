from selenium.webdriver.common.by import By

from tests_allure.pages.BasePage import BasePage


class AlertElement(BasePage):
    POPUP = (By.CSS_SELECTOR, ".alert-success")
    COMPARISON = (By.LINK_TEXT, "product comparison")
    LOGIN = (By.LINK_TEXT, "login")
    CART = (By.LINK_TEXT, "shopping cart")

    def popup_alert(self):
        return self.element(self.POPUP)

    @property
    def comparison(self):
        return self.element(self.COMPARISON)

    @property
    def login(self):
        return self.element(self.LOGIN)

    @property
    def cart(self):
        return self.element(self.CART)
