from tests_allure.tests.lib.constant_login_page import LoginForPage
from tests_allure.pages.LoginPage import LoginPage
import pytest
import allure

TEST_CASE_LINK = 'http://localhost/'


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

# def test_failure():
#     """this test fails"""
#     assert 1  # -> AssertionError
#
#
# def test_failure2():
#     """this test fails"""
#     assert 0  # -> AssertionError
#
#
# @pytest.mark.skip(reason="Broken")
# def test_skip():
#     """this test is skipped"""
#     pytest.skip('for a reason!')
#
#
# @allure.link('https://docs.qameta.io/allure/#_pytest')
# def test_with_link():
#     pass
#
#
# @allure.link('https://docs.qameta.io/allure/#_pytest', name='I am custom link name')
# def test_with_named_link():
#     pass
#
#
# @pytest.mark.skip(reason="JIRA-9000")
# @allure.issue('https://pytest.org', 'Pytest-flaky test retries shows like test steps')
# def test_with_issue_link():
#     assert False
