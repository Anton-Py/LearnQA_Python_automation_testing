from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import logging
import pytest
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = driver.base_url
        # self.logger = driver.logger

        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"tests/logs/{self.driver.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.driver.log_level)

    def element(self, locator: tuple, time=0.1, ):
        self.logger.info("Find visibility element: {}".format(locator))
        try:
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image")
            raise AssertionError(f"Can't find element by locator {locator}", e.msg)

    def elements(self, locator: tuple, time=0.1):
        self.logger.info("Find visibility elements: {}".format(locator))
        try:
            return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException as e:
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image")
            raise AssertionError(f"Can't find element by locator {locator}", e.msg)

    def elements_pr(self, locator: tuple, time=0.1):
        self.logger.info("Find presence element: {}".format(locator))
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException as e:
            raise AssertionError(f"Can't find element by locator {locator}", e.msg)

    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        self.logger.info(
            "Find the element {} and click on the element {} inside it".format(parent_locator, child_locator))
        return self.element(parent_locator).find_element(*child_locator)

    def elements_in_element(self, parent_locator: tuple, child_locator: tuple):
        self.logger.info(
            "Find the element {} and click on the elements {} inside it".format(parent_locator, child_locator))
        return self.element(parent_locator).find_elements(*child_locator)

    def check_element(self, locator):
        self.logger.info("Clicking element: {}".format(locator))
        return self.element(locator)

    def coll_elements(self, locator):
        self.logger.info("Click to search multiple items: {}".format(locator))
        return self.elements(locator)

    def _click(self, element):
        self.logger.info("Click element: {}".format(element))
        ActionChains(self.driver).move_to_element(element).pause(0.3).click().perform()

    def check_alert(self):
        self.logger.info("Check browser pop-up")
        alert = WebDriverWait(self.driver, 2).until(EC.alert_is_present())
        alert.accept()

    def _input(self, element, value):
        self.logger.info("Enter data into input: element = {}, value = {}".format(element, value))
        self._click(element)
        element.clear()
        element.send_keys(value)
