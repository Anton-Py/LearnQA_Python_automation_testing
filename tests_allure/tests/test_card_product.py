from tests_allure.tests.lib.constant_card_product import CardForProduct
from tests_allure.pages.CardProduct import CardProduct


def test_main_page(browser):
    page = CardProduct(browser)
    page.open()
    assert browser.title == CardForProduct.TITLE_MAIN_PAGE
    page.click_card_product_product_link()
    assert browser.title == CardForProduct.TITLE_PRODUCT_PAGE
    assert len(page.coll()) == 5
    page.check_element_button()
    page.check_element_field()
    page.click_card_product_description()
    page.click_card_product_specification()
    page.click_card_product_revirws()
