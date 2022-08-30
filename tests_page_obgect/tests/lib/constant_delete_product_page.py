from selenium.webdriver.common.by import By


class DeleteForProductPage:
    TABLE_STR = (By.CSS_SELECTOR, '#form-product > div > table > tbody > tr')
    CHECKBOX = (By.CSS_SELECTOR, '[type="checkbox"]')
    BUTTON_DELETE = (By.CSS_SELECTOR, '[class="fa fa-trash-o"]')
