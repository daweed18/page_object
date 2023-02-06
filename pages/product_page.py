from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_see_add_to_card_button()
        self.should_see_title()
        self.should_see_price()

    def should_see_title(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), "Элемента заголовок нету"

    def should_see_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Элемента цена нету"

    def should_see_add_to_card_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CARD_BUTTON), "Кнопки добавить в корзину нету"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение присутствует на сайте"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение не исчезло"

    def get_title(self):
        if self.is_element_present(*ProductPageLocators.PRODUCT_TITLE):
            return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_price(self):
        if self.is_element_present(*ProductPageLocators.PRICE):
            return self.browser.find_element(*ProductPageLocators.PRICE).text

    def add_to_card(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BUTTON)
        button.click()

    def get_price_after_add_to_card(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_AFTER_ADD).text
        title = self.browser.find_element(*ProductPageLocators.TITLE_AFTER_ADD).text
        return price, title