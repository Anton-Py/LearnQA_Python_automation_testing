from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_of_element(driver, css_selector, time=1.5):
    return WebDriverWait(driver, time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)),
        message=f"Can't find element by locator {css_selector}")


def wait_of_elements(driver, css_selector, time=1.5):
    return WebDriverWait(driver, time).until(
        EC.visibility_of_any_elements_located((By.CSS_SELECTOR, css_selector)),
        message=f"Can't find element by locator {css_selector}")


def wait_of_elements_link(driver, css_selector, time=1.5):
    return WebDriverWait(driver, time).until(
        EC.visibility_of_any_elements_located((By.LINK_TEXT, css_selector)),
        message=f"Can't find element by locator {css_selector}")


def wait_of_element_link(driver, css_selector, time=1.5):
    return WebDriverWait(driver, time).until(
        EC.visibility_of_element_located((By.LINK_TEXT, css_selector)),
        message=f"Can't find element by locator {css_selector}")
