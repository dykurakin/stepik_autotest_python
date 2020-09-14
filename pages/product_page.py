from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_btn.click()

    def should_be_product_name_in_basket_equal_on_page(self):
        prod_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        prod_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert (prod_name == prod_name_in_basket), "Product is not added in basket"

    def should_be_basket_price_product(self):
        prod_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert (prod_price == basket_price), "Basket price is not correct"