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

# def test_hello_selenium_mov(driver):
#     driver.get(url=driver.base_url)
#     elem = wait_of_element(driver, ".pull-to-end>a:nth-child(1)")
#     print(elem.tag_name, end="\n")
#     print(elem.parent)
#     print(elem.get_attribute("class"))
#     print(elem.get_property("tagName"))
#     print(elem.get_property("isConnected"))
#     print(elem.value_of_css_property("color"))
#     print(elem.value_of_css_property("background-color"))
#     print(elem.text)
#     print(elem.size)
#     print(elem.rect)
#     print(elem.screenshot("test.png"))
#     print(dir(elem))
#     for f in dir(elem):
#         print(f)
#     # time.sleep(2)
import random, string


# def test_create_random_words():
#     a = []
#     for f in range(2):
#         a.append(random.choice(string.ascii_letters))
#         print("".join(a))
#
#     b = "".join(random.choice(string.ascii_letters) for f in range(2))
#     print(b)


# def test_random_email():
#     domains = ['ru', 'com', 'de']
#     names = ['round', 'texas', 'kent']
#
#     def create_random_int():
#         return random.randint(100, 999)
#
#     def create_random_words():
#         return "".join(random.choice(string.ascii_letters) for f in range(2))
#
#     def random_domain():
#         return random.choice(domains)
#
#     def random_name():
#         return random.choice(names)
#
#     email = f"{random_name()}.{create_random_int()}@{create_random_words()}.{random_domain()}"
#     print(email)


# import random, string

# def test():
#     print(f"{random.choice(['king','miller','kean'])}.{random.randint(100,999)}@{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5,7+1))}.{random.choice(['net','com','ua'])}")


def test(browser):
    browser.get(url="http://localhost/")
    time.sleep(5)
    print(browser.find_element(By.CSS_SELECTOR, '.navbar-nav>li:nth-child(1)'))
    print(browser.find_elements(By.CSS_SELECTOR, '.navbar-nav>li'))
