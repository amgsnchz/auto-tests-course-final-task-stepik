from selenium.webdriver.common.by import By


class MainPageLocators:  # каждый селектор — это пара: как искать и что искать!
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')  # селектор на переход на страницу логина


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')  # Селектор на форму логина
    REG_FORM = (By.CSS_SELECTOR, '#register_form')  # Селектор на форму регистрации
