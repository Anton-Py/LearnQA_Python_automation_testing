from selenium.webdriver.common.by import By


class MainForPage:
    TITLE_MAIN_PAGE = "Your Store"
    GENERAL_ELEM_NAVBAR = (By.CSS_SELECTOR, ".navbar-collapse")
    ELEM_NAVBAR_FOR_CHOISE = (By.CSS_SELECTOR, '.navbar-nav>li')
    BUTTON_ACCOUNT = (By.CSS_SELECTOR, ".list-inline .dropdown")
    LINK_REGISTER = (By.LINK_TEXT, "Register")
    LINK_LOGIN = (By.LINK_TEXT, "Login")
    VALUE_SEARCH = "main"
    ELEM_PRODUCT = (By.CSS_SELECTOR, ".product-thumb")
    FIELD_SEARCH = (By.CSS_SELECTOR, "#search .form-control")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "#search button")
    TITLE_SEARCH_PAGE = "Search - main"
    CHECKBOX_DESCRIPTION = (By.CSS_SELECTOR, '[class="checkbox-inline"] [name="description"]')
    BLUE_BUTTON_SEARCH = (By.CSS_SELECTOR, '[value="Search"]')
    ELEM_PRODUCT_SEARCH = (By.CSS_SELECTOR, ".product-thumb")
