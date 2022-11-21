from .base_page import BasePage
from .locators import BascetPageLocators, ProductPageLocators


class BascetPage(BasePage):
    """Тесты для страницы с корзиной товаров"""
    def add_product_in_bascet(self):
        """Добавление товара в корзину"""
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASCET)
        link.click()

    def bascet_is_empty_text_is_present(self):
        """Проверка на наличие сообщения о пустой корзине"""
        assert self.is_element_present(*BascetPageLocators.EMPTY_BASCET), "bascet is not empty"

    def should_not_be_product_add(self):
        """Проверка на отсутвие товара в корзине"""
        assert self.is_not_element_present(*BascetPageLocators.PRICE_TO_ONE_PRODUCT), \
            "Buscet is no empty"
