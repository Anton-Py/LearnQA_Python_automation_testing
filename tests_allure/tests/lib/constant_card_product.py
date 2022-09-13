from selenium.webdriver.common.by import By


class CardForProduct:
    TITLE_MAIN_PAGE = "Your Store"
    TITLE_PRODUCT_PAGE = "MacBook"
    PRODUCT_LINK = (By.LINK_TEXT, "MacBook")
    DESCRIPTION_LINK = (By.LINK_TEXT, "Description")
    SPECIFICATION_LINK = (By.LINK_TEXT, "Specification")
    REVIRWS_LINK = (By.LINK_TEXT, "Reviews (0)")
    CARD_CHARACTERISTICS = (By.CSS_SELECTOR, ".thumbnails li")
    FIELD_QUANTITITY = (By.CSS_SELECTOR, '.form-group [name="quantity"]')
    BUY_BUTTON = (By.CSS_SELECTOR, "#product #button-cart")
