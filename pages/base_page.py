from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    """Тесты и методы для всех страниц ресурса"""
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Открыть страницу"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """Элемент должен присутствовать на странице"""

        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Элемент должен отсутствовать на странице"""

        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        """Элемент должен исчезнуть со страницы"""
        try:
            WebDriverWait(self.browser, timeout, 1). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        """Перейти на страницу с авторизацией/регистрацией"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        """Должна присутсвовать ссылка на авторизацию/регистрацию"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_from_any_page_to_bascet_page(self):
        """Переход с любой страницы в корзину"""
        link = self.browser.find_element(*BasePageLocators.BUTTON_BASCET)
        link.click()

    def should_be_authorized_user(self):
        """Проверка на то, что пользователь авторизован"""
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
