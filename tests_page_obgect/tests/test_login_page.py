from tests_page_obgect.tests.lib.constant_login_page import LoginForPage
from tests_page_obgect.pages.LoginPage import LoginPage


def test_login_page(driver):
    LoginPage(driver).open()
    assert driver.title == LoginForPage.TITLE_LOGIN_PAGE
    assert len(LoginPage(driver).coll()) == 2
    LoginPage(driver).check_element_password()
    LoginPage(driver).login()
    assert driver.title == LoginForPage.TITLE_SUCCESS
