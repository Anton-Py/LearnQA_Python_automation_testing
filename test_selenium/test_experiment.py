# def test_hello_selenium1(driver):
#     driver.get(url=driver.base_url)
#     assert driver.title == "Your Store"
#
#
# def test_hello_selenium2(driver):
#     driver.get(url=driver.base_url)
#     # driver.save_screenshot("test.png")
#     assert driver.title == "YourStore"
import time
from test_selenium.tests.lib.constant_register_page import RegisterPage
from test_selenium.tests.lib.waitings import *


def test_hello_selenium_mov(driver):
    driver.get(url=driver.base_url)
    elem = wait_of_element(driver, ".pull-to-end>a:nth-child(1)")
    print(elem.tag_name, end="\n")
    print(elem.parent)
    print(elem.get_attribute("class"))
    print(elem.get_property("tagName"))
    print(elem.get_property("isConnected"))
    print(elem.value_of_css_property("color"))
    print(elem.value_of_css_property("background-color"))
    print(elem.text)
    print(elem.size)
    print(elem.rect)
    print(elem.screenshot("test.png"))
    print(dir(elem))
    for f in dir(elem):
        print(f)
    # time.sleep(2)

