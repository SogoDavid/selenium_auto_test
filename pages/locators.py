from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы для глаавной страницы"""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    """Локаторы для страницы с авторизацией/регистрацией"""

    URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD_ACCEPT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators:
    """Локаторы для страницы с продуктами"""

    URL = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    BUTTON_ADD_TO_BASCET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    INFO_ADD_PRODUCT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > .alertinner > strong")
    INFO_BASCET_PRICE = (By.CSS_SELECTOR, ".alertinner > p:nth-child(1) > strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main > .price_color")
    MAIN_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    BUTTON_REPLACE_TO_BASCET = (By.CSS_SELECTOR, ".btn-info.btn-sm")

class BascetPageLocators:
    """Локаторы для страницы с корзиной"""

    URL = "http://selenium1py.pythonanywhere.com/basket/"
    FULL_PRICE_TO_BYE = (By.CSS_SELECTOR, ".col-sm-2 > .price_color.align-right")
    PRICE_TO_ONE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-1 > .price_color.align-right")
    EMPTY_BASCET = (By.CSS_SELECTOR, "#content_inner>p")

class BasePageLocators:
    """Общие локаторы для всех страниц"""

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASCET = (By.CSS_SELECTOR, ".btn-group>a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
