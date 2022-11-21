from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.bascet_page import BascetPage
import pytest

"""Тест-кейсы для главной страницы"""

@pytest.mark.need_review
@pytest.mark.login_guest
class TestLoginFormMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        """Гость может зайти в страниу для авторизации"""

        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        """На странице отображена ссылка для авторизации"""

        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

@pytest.mark.need_review
def test_word_login_present_in_url(browser):
    """Слово login представлено в url"""

    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

@pytest.mark.need_review
def test_should_present_login_form(browser):
    """Проверка на наличие формы для авторизации"""

    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

@pytest.mark.need_review
def test_should_present_registration_form(browser):
    """Проверка на наличие формы для регистрации"""

    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """Гость открывает с главной страницы пустую корзину
     и должен увидеть сообщение, о том что корзина пуста"""

    link = "http://selenium1py.pythonanywhere.com"
    page = LoginPage(browser, link)
    sec_page = BascetPage(browser, link)
    page.open()
    page.go_from_any_page_to_bascet_page()
    sec_page.should_not_be_product_add()
    sec_page.bascet_is_empty_text_is_present()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Гость открывает с продуктовой страницы пустую корзину
         и должен увидеть сообщение, о том что корзина пуста"""

    link = "https://selenium1py.pythonanywhere.com/catalogue"
    page = LoginPage(browser, link)
    sec_page = BascetPage(browser, link)
    page.open()
    page.go_from_any_page_to_bascet_page()
    sec_page.should_not_be_product_add()
    sec_page.bascet_is_empty_text_is_present()

