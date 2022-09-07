from selenium.webdriver.common.by import By


class CatalogForPage:
    TITLE_MAIN_PAGE = "Your Store"
    TITLE_CATALOG_PAGE = "MP3 Players"
    TAB_MP3 = (By.CSS_SELECTOR, ".navbar-nav>li:nth-child(8)")
    TAB_SEE_ALL = (By.CSS_SELECTOR, "li:nth-child(8) .see-all")
    ELEM_PRODUCT = (By.CSS_SELECTOR, ".product-thumb")
    COLL_GROUP_ELEMENTS = (By.CSS_SELECTOR, ".list-group a")
    GROUP_AFTER_CLICK = (By.CSS_SELECTOR, '[class="breadcrumb"] li:nth-child(3)')
