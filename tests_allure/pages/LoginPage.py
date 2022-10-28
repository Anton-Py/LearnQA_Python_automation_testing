from tests_allure.tests.lib.constant_login_page import LoginForPage
from tests_allure.pages.BasePage import BasePage
import pytest
import allure


class LoginPage(BasePage):
    path = "/admin"

    @allure.step("Открываем страницу авторизации")
    def open(self):
        self.logger.info("Opening url: {}".format(self.base_url + self.path))
        self.driver.get(self.base_url + self.path)

    @allure.step("Получаем количество элементов")
    def coll(self):
        return self.coll_elements(LoginForPage.SELECTOR_FIELD)

    @allure.step("Проверяю наличие псообщения ошибки при невалидных данных пароль/логин")
    def check_element_alert(self):
        self.check_element(LoginForPage.ALERT_MESSAGE)

    @allure.step("Проверяю наличие поля пароль")
    def check_element_password(self):
        self.check_element(LoginForPage.FORGOTTEN_LINK)

    @allure.step("Проверяю наличие кнопки логаут")
    def check_button_logout(self):
        self.check_element(LoginForPage.BUTTON_LOGOUT)

    @allure.step("Находим элементы которые содержит меню")
    def find_elements_menu(self):
        return self.elements_in_element(LoginForPage.ELEMENT_MENU, LoginForPage.ELEM_IN_MENU)

    @allure.step("Водим валидные данные в фому логирования")
    def login(self):
        self._input(self.element(LoginForPage.FIELD_USERNAME), LoginForPage.USERNAME)
        self._input(self.element(LoginForPage.FIELD_PASSWORD), LoginForPage.PASSWORD)
        self._click(self.element(LoginForPage.BUTTON_LOGIN))

    @allure.step("Водим невалидные данные в фому логирования")
    def login_with_incorrect_data(self, user, password):
        self._input(self.element(LoginForPage.FIELD_USERNAME), user)
        self._input(self.element(LoginForPage.FIELD_PASSWORD), password)
        self._click(self.element(LoginForPage.BUTTON_LOGIN))
