import random
from selenium.webdriver.common.by import By

currency = [(By.CSS_SELECTOR, '[name="GBP"]'), (By.CSS_SELECTOR, '[name="EUR"]'), (By.CSS_SELECTOR, '[name="USD"]')]


def get_currency():
    return random.choice(currency)
