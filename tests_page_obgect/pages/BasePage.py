from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = driver.base_url

    def element(self, locator: tuple, time=1.5):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def elements(self, locator: tuple, time=1.5):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Can't find element by locator {locator}")

    def elements_pr(self, locator: tuple, time=1.5):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find element by locator {locator}")

    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        return self.element(parent_locator).find_element(*child_locator)

    def elements_in_element(self, parent_locator: tuple, child_locator: tuple):
        return self.element(parent_locator).find_elements(*child_locator)

    def check_element(self, locator):
        return self.element(locator)

    def coll_elements(self, locator):
        return self.elements(locator)

    def _click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.3).click().perform()

    def check_alert(self):
        alert = WebDriverWait(self.driver, 2).until(EC.alert_is_present())
        alert.accept()

    def _input(self, element, value):
        self._click(element)
        element.clear()
        element.send_keys(value)
