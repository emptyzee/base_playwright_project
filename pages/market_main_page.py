from pages.base import Base
from Locators.basket_page import Basket
from Locators.market_page import Market
from data.assertions import Assertions
from playwright.sync_api import Page


class MarketPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)


    def add_to_cart(self):
        self.click_element_by_index(Market.ADD_TO_CART, 0) #кликаем по индексу, 0 это значит, что кликаем по первой карточке
        self.click(Market.FOLLOW_TO_BASKET)

    def checkout(self):
        self.click(Basket.CHECKOUT_BTN)
        self.input(Basket.FIRST_NAME, "Ivan")
        self.input(Basket.LAST_NAME, "Ivanov")
        self.input(Basket.ZIP, "123456")
        self.click(Basket.CNT_BTN)
        self.click(Basket.FINISH_BTN)
        self.assertions.have_text(Basket.FINAL_TEXT, "Checkout: Complete!", "no")