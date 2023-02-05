from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_see_add_to_card_button()
        self.should_see_title()
        self.should_see_price()
        self.add_to_card()

    def should_see_title(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE)

    def should_see_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE)

    def should_see_add_to_card_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CARD_BUTTON)

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