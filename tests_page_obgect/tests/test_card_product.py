from tests_page_obgect.tests.lib.constant_card_product import CardForProduct
from tests_page_obgect.pages.CardProduct import CardProduct


def test_main_page(driver):
    CardProduct(driver).open()
    assert driver.title == CardForProduct.TITLE_MAIN_PAGE
    CardProduct(driver).click_card_product_product_link()
    assert driver.title == CardForProduct.TITLE_PRODUCT_PAGE
    assert len(CardProduct(driver).coll()) == 5
    CardProduct(driver).check_element_button()
    CardProduct(driver).check_element_field()
    CardProduct(driver).click_card_product_description()
    CardProduct(driver).click_card_product_specification()
    CardProduct(driver).click_card_product_revirws()
