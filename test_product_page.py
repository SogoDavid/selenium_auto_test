import time
import allure
import pytest
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

"""Тест-кейсы для страницы с продуктами"""


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.parametrize('offer', [page for page in range(10)])
@allure.story("Добавление товара в корзину")
def test_cost_basket_coincides_with_price_goods(browser, offer):
    """Добаваление товара в корзину, прохождение двух алертов,
    проверка на появление окна об успехе с ценой и наименованием"""

    flink = f"""http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer{offer}"""
    page = ProductPage(browser, flink)
    page.open()
    if offer == 7:
        pytest.xfail()
    page.add_product_in_bascet()
    page.solve_quiz_and_get_code()
    page.should_be_product_price_equal_bascet_price()
    page.should_be_product_add_to_bascet()


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.xfail
@allure.story("Отображение элементов страницы")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Гость должен увидеть уведомление о том, что товар добавлен
              в корзину, но в тесте есть ошибка, XFail"""

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_bascet()
    page.should_not_be_success_message()


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@allure.story("Отображение элементов страницы")
def test_guest_cant_see_success_message(browser):
    """Товар не добавлен в корзину, поэтому должно отсутсвовать
          сообщение о том, что товар добавлен в корзину"""

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.xfail
@allure.story("Отображение элементов страницы")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Сообщение об успешном добавлении товара в корзину
            должно исчезнуть, но оно не исчезает"""

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_bascet()
    page.element_disappear()


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@allure.story("Отображение элементов страницы")
def test_guest_should_see_login_link_on_product_page(browser):
    """Гость должен видеть кнопку с ссылкой на авторизацию"""

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@allure.story("Переходы между страницами")
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Гость может перейти на страницу с авторизацией со страницы с продуктами"""

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.smoke
@allure.story("Добавление товара в корзину")
class TestUserAddToBasketFromProductPage:

    @pytest.mark.xfail(reason="Server error")
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """Регистрация пользователя"""

        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "Stepik132456"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @allure.severity(allure.severity_level.NORMAL)
    def test_user_cant_see_success_message(self, browser):
        """Зарегистрированый пользователь не добавил товар в корзину,
        поэтому должно отсутсвовать сообщение об успешном добавлении"""

        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_add_product_to_basket(self, browser):
        """Зарегистрированный пользователь должен иметь доступ
                    к добавлению товара в корзину"""

        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_in_bascet()
        page.should_be_product_price_equal_bascet_price()
        page.should_be_product_add_to_bascet()
