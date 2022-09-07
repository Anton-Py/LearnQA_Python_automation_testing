from tests_page_obgect.pages.AddProductPage import AddProductPage
from tests_page_obgect.pages.DeleteProductPage import DeleteProductPage
from tests_page_obgect.pages.LoginPage import LoginPage


def test_login_page(driver):
    LoginPage(driver).open()
    LoginPage(driver).login()
    AddProductPage(driver).click_catalog()
    AddProductPage(driver).select_tab_product()
    DeleteProductPage(driver).find_product()
    DeleteProductPage(driver).add_delete()
    DeleteProductPage(driver).check_alert()
