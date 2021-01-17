from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def register_new_user(self, email, password):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_ENTER).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, '"login" not in the current url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'There is no login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), 'There is no register form'
