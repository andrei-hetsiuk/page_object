from .base_page import BasePage
from .locators import ProductPageLocators

import time


class ProductPage(BasePage):
    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_BOOK)
        login_link.click()
        time.sleep(2)

    def should_be_book_added(self):
        assert self.browser.find_element(
            *ProductPageLocators.MESSAGE_ADDED_BOOK), "the message the book is not presented"
        book_titel = self.browser.find_element(*ProductPageLocators.BOOK_TITEL).text
        book_titel_message = self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_TITEL).text
        assert book_titel == book_titel_message, "book titel is not the same in the message about books added to the " \
                                                 "basket "

    def should_be_cost_the_same_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST).text
        print(book_price)
        print(basket_cost)
        assert basket_cost == book_price, "book price is not the same as basket cost"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_BOOK_TITEL), \
            "Success message is presented, but should not be"

    def should_not_be_present_book(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_BOOK), \
            "The book is presented, but should not be"

    def should_message_dissapeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADDED_BOOK), \
            "The book is presented, but should not be"
