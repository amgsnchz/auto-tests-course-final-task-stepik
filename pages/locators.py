from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    ITEM_NAME = (By.CSS_SELECTOR, "div[class = \"col-sm-6 product_main\"] > h1")
    ITEM_ADDED_TEXT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_COST = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")
    ITEM_COST = (By.CSS_SELECTOR, "p.price_color")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    CART_LINK = (By.CSS_SELECTOR, '.btn-group')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    PRODUCT = (By.CSS_SELECTOR, '.basket-items')
    BASKET_STATUS = (By.CSS_SELECTOR, '#content_inner > p')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASS = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_ENTER = (By.CSS_SELECTOR, 'name="login_submit"')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASS1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_ENTER = (By.CSS_SELECTOR, '[value=Register]')
