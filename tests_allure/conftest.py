import pytest
import logging
import datetime
import os

from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="browser to run test")
    parser.addoption("--drivers", default=os.path.expanduser("~/drivers"), help="browser to run test")
    parser.addoption("--headless", action="store_false", help="browser to run test")
    parser.addoption("--base_url", default="http://localhost/", help="browser to run test")
    # parser.addoption('--window_size', default='1300, 1080', help='Enter window size.')
    parser.addoption("--window-size", nargs=2, default=["1600", "1000"], help="browser to run test")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption("--browser")
    drivers_folder = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")
    window_size = request.config.getoption("--window-size")
    # window_size = map(int, request.config.getoption('--window_size').split(','))
    log_level = request.config.getoption("--log_level")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        if window_size:
            options.start_maximized = True
        driver = webdriver.Chrome(
            executable_path=os.path.expanduser(f"{drivers_folder}/chromedriver"),
            options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=os.path.expanduser(f"{drivers_folder}/geckodriver"))
    else:
        raise ValueError(f"Browse {browser_name} is not supported.")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"tests/logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    driver.base_url = base_url
    driver.set_window_size(*window_size)

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver
