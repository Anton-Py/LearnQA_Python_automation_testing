from selenium.webdriver.common.by import By


class LoginForPage:
    TITLE_LOGIN_PAGE = "Administration"
    SELECTOR_FIELD = (By.CSS_SELECTOR, '[class="input-group"]')
    FIELD_USERNAME = (By.CSS_SELECTOR, '[type="text"][name="username"]')
    FIELD_PASSWORD = (By.CSS_SELECTOR, '[type="password"][name="password"]')
    USERNAME = "user"
    PASSWORD = "bitnami"
    BUTTON_LOGIN = (By.CSS_SELECTOR, '[type="submit"]')
    FORGOTTEN_LINK = (By.CSS_SELECTOR, '[class="help-block"]')
    TITLE_SUCCESS = 'Dashboard'
