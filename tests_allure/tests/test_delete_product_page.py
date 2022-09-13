from tests_allure.pages.AddProductPage import AddProductPage
from tests_allure.pages.DeleteProductPage import DeleteProductPage
from tests_allure.pages.LoginPage import LoginPage


def test_delete_page(browser):
    page_log = LoginPage(browser)
    page_add = AddProductPage(browser)
    page_del = DeleteProductPage(browser)
    page_log.open()
    page_log.login()
    page_add.click_catalog()
    page_add.select_tab_product()
    page_del.find_product()
    page_del.add_delete()
    page_del.check_alert()
