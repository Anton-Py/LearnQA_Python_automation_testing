from tests_allure.tests.lib.constant_login_page import LoginForPage
from tests_allure.pages.LoginPage import LoginPage
import pytest
import allure

TEST_CASE_LINK = 'https://hub.docker.com/r/bitnami/opencart'


@allure.title('logging to system')
@allure.testcase(TEST_CASE_LINK, 'Test case title')
@allure.link('http://localhost/', name="Login in opencart")
@pytest.mark.parametrize('coll_cards', [2, 3], ids=['Истина', 'Ложь'])
@pytest.mark.parametrize('coll_elements_menu', [9, 5], ids=['Истина', 'Ложь'])
def test_login_page(browser, coll_cards, coll_elements_menu):
    page = LoginPage(browser)
    page.open()
    assert len(page.coll()) == coll_cards
    page.check_element_password()
    page.login()
    assert len(page.find_elements_menu()) == coll_elements_menu
    page.check_button_logout()
    assert browser.title == LoginForPage.TITLE_SUCCESS


@pytest.mark.parametrize('user, password', [(LoginForPage.USERNAME, LoginForPage.INCORRECT_PASSWORD),
                                            (LoginForPage.INCORRECT_USERNAME, LoginForPage.PASSWORD)])
def test_login_page_with_incorrect_data(browser, user, password):
    page = LoginPage(browser)
    page.open()
    assert len(page.coll()) == 2
    page.check_element_password()
    page.login_with_incorrect_data(user, password)
    page.check_element_alert()
