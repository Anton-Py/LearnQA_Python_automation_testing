from selenium.webdriver.common.by import By


class CheckForCurrencyPage:
    BUTTON_CURRENCY = (By.CSS_SELECTOR, '#form-currency .btn-group>button')
    CHILD_SELECTOR = (By.CSS_SELECTOR, 'button Strong')
    SYMBOL_CURRENCY = (By.CSS_SELECTOR, '[class="price"]')

