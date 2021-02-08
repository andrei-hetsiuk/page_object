from .base_page import BasePage
from .locators import ProductPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_TITEL), "book is not presented"

    def should_be_empty_basket_text(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_EMPTY_TEXT).text, "no empty basket text"
