from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON).click()

    def should_not_be_success_message_is_not_element_present(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'

    def should_not_be_success_message_element_is_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'

    def add_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_item_in_the_basket(self):
        if not self.is_element_present(*ProductPageLocators.ITEM_ADDED_TEXT):
            assert self.is_element_present(
                *ProductPageLocators.ITEM_ADDED_TEXT), "'Added to basket' message is not presented"
        else:
            item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
            item_add_text = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_TEXT)
            assert item_name.text == item_add_text.text, \
                f"Item name '{item_add_text.text}' in message 'added to basket' message is incorrect"

    def should_be_correct_basket_cost(self):
        if not self.is_element_present(*ProductPageLocators.BASKET_COST):
            assert self.is_element_present(
                *ProductPageLocators.BASKET_COST), "'Your basket total' message is not presented"
        else:
            item_cost = self.browser.find_element(*ProductPageLocators.ITEM_COST)
            basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST)
            assert item_cost.text == basket_cost.text, \
                f"Basket cost '{basket_cost.text}' in 'Your basket total' message is incorrect"
