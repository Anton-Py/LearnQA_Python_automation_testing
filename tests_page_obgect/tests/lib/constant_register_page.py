from selenium.webdriver.common.by import By


class RegisterForPage:
    TITLE_REGISTER_PAGE = "Register Account"
    LIST_GROUP = (By.CSS_SELECTOR, '[class="list-group"] a')
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, '[type="text"][name="firstname"]')
    FIELD_LAST_NAME = (By.CSS_SELECTOR, '[type="text"][name="lastname"]')
    FIELD_EMAIL = (By.CSS_SELECTOR, '[type="email"][name="email"]')
    FIELD_TELEPHONE = (By.CSS_SELECTOR, '[type="tel"][name="telephone"]')
    FIRST_NAME = "Testing-"
    LAST_NAME = "ForTesting-"
    EMAIL = "cbozog@mailto.plus"
    TELEPHONE = '891300874'
    FIELD_PASSWORD = (By.CSS_SELECTOR, '[type="password"][name="password"]')
    FIELD_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '[type="password"][name="confirm"]')
    PASSWORD = 'TestTest22'
    BUTTON_CONTINUE = (By.CSS_SELECTOR, '[type="submit"][value="Continue"]')
    CHECKBOX_PRIVACY_POL = (By.CSS_SELECTOR, '[type="checkbox"]')
    TITLE_SUCCESS = "Your Account Has Been Created!"
