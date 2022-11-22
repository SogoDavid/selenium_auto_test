from time import sleep

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Тесты и методы для страницы с авторизацией и регистрацией"""
    def should_be_login_page(self):
        """Список обязательных тестов для страницы с авторизацией/регистрацией"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверка, о наличии эндпоинта login в url ресурса"""

        assert "/login" in self.browser.current_url, "Missed 'login' im url of syte"

    def should_be_login_form(self):
        """Проверка на наличие поля логина"""

        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """Проверка на наличие поля регистрации"""

        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        """Регистрация нового пользователя"""

        self.browser.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_ACCEPT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()
        sleep(2)
