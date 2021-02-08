from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR,"#id_registration-email")
    PASS = (By.CSS_SELECTOR,"#id_registration-password1")
    PASS_CONFIRM = (By.CSS_SELECTOR,"#id_registration-password2")
    SUBMIT_BUTTON = (By.CSS_SELECTOR,'button[name|="registration_submit"]')

class ProductPageLocators:
    ADD_BOOK = (By.CSS_SELECTOR, "#add_to_basket_form")
    MESSAGE_ADDED_BOOK =(By.CSS_SELECTOR, "#messages")
    BOOK_TITEL = (By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_BOOK_TITEL = (By.CSS_SELECTOR,".alert-success strong")
    BOOK_PRICE = (By.CSS_SELECTOR,".product_main p")
    BASKET_COST = (By.CSS_SELECTOR,".alert-info p strong")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR,"#content_inner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


