import pytest
import os

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="browser to run test")
    parser.addoption("--drivers", default=os.path.expanduser("~/drivers"), help="browser to run test")
    parser.addoption("--headless", action="store_true", help="browser to run test")
    parser.addoption("--base_url", default="http://localhost/", help="browser to run test")
    # parser.addoption('--window_size', default='1300, 1080', help='Enter window size.')
    parser.addoption("--window-size", nargs=2, default=["1600", "1000"], help="browser to run test")


@pytest.fixture(scope='session')
def driver(request):
    browser_name = request.config.getoption("--browser")
    drivers_folder = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")
    window_size = request.config.getoption("--window-size")
    # window_size = map(int, request.config.getoption('--window_size').split(','))
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        if window_size:
            options.start_maximized = True
        _driver = webdriver.Chrome(
            executable_path=os.path.expanduser(f"{drivers_folder}/chromedriver"),
            options=options)
    elif browser_name == "firefox":
        _driver = webdriver.Firefox(executable_path=os.path.expanduser(f"{drivers_folder}/geckodriver"))
    else:
        raise ValueError(f"Browse {browser_name} is not supported.")

    _driver.base_url = base_url
    _driver.set_window_size(*window_size)

    yield _driver

    _driver.close()
