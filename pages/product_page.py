import math
from time import sleep

from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Тесты для продуктовой страницы"""
    def add_product_in_bascet(self):
        """Нажатие на кнопку 'добавить товар в корзину'"""

        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASCET)
        link.click()

    def solve_quiz_and_get_code(self):
        """Обработка всплывающего окна(алерта)"""

        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        sleep(4)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()

        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_product_price_equal_bascet_price(self):
        """Проверка соответсвия цены добавленного товара с суммой в корзине"""
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        info_bascet_price = self.browser.find_element(*ProductPageLocators.INFO_BASCET_PRICE)
        assert price_product.text in info_bascet_price.text, "Стоимость товара, не совпадает с суммой в корзине товаров"

    def should_be_product_add_to_bascet(self):
        """Проверка, что наименование добавленного товара
         соответсвует сообщению с именем добавленного товара"""

        info_add_product = self.browser.find_element(*ProductPageLocators.INFO_ADD_PRODUCT)
        main_product = self.browser.find_element(*ProductPageLocators.MAIN_PRODUCT)
        assert main_product.text == info_add_product.text, "Информация о добавленном товаре," \
                                                           " не соответствует наименованию товара"

    def should_not_be_success_message(self):
        """Проверка отсутсвия сообщения, о том что товар добавлен в корзину"""

        assert self.is_not_element_present(*ProductPageLocators.INFO_ADD_PRODUCT), \
            "Success message is presented, but should not be"

    def element_disappear(self):
        """Проверка исчезновения сообщения, о том что товар добавлен в корзину"""

        assert self.is_disappeared(*ProductPageLocators.INFO_ADD_PRODUCT), \
            "Элемент не исчезает"



