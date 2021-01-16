from pages.main_page import MainPage
from pages.login_page import LoginPage


def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector('#login_link')
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()  # выполняем проверку should_be_login_page из класса BasePage
    # (MainPage наследник его и наследует все его методы)


def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)  # инициализируем класс MainPage, передаем в конструктор экземпляр драйвера и
    # url адрес
    page.open()  # открываем страницу методом (функцией) open из класса MainPage
    page.should_be_login_link()  # выполняем проверку should_be_login_link из класса BasePage
    # (MainPage наследник его и наследует все его методы)
