from selenium.webdriver.common.by import By


class AddForProductPage:
    TITLE_LOGIN_PAGE = "Administration"
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    ELEMENT_PRODUCT = (By.LINK_TEXT, "Products")
    BUTTON_PLUS = (By.CSS_SELECTOR, '[class="fa fa-plus"]')
    FIELD_NAME = (By.CSS_SELECTOR, '[name="product_description[1][name]"]')
    NAME_PRODUCT = "Phone Samsung"
    FIELD_META = (By.CSS_SELECTOR, '[name="product_description[1][meta_title]"]')
    META_PRODUCT = "Title Meta Product"
    FIELD_DESCRIPTION = (By.CSS_SELECTOR, '[class="note-editable"]')
    DESCRIPTION_PRODUCT = 'Good model'
    NAVBAR = (By.LINK_TEXT, 'Data')
    FIELD_MODEL = (By.CSS_SELECTOR, '[name="model"]')
    MODEL_PRODUCT = "N70"
    FIELD_PRICE = (By.CSS_SELECTOR, '[name="price"]')
    PRICE_PRODUCT = '100'
    BUTTON_SAVE = (By.CSS_SELECTOR, '[class="fa fa-save"]')
