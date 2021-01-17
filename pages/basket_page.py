from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), 'Basket is not empty, but should be'

    def basket_is_empty_message(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_STATUS).text
        assert message.count('empty') != 0
