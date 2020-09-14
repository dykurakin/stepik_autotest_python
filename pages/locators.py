from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//div/h1")
    PRODUCT_NAME_IN_BASKET = (By.XPATH, "//*[text()[contains(.,'added to your basket.')]]/strong")
    PRODUCT_ADDED_IN_BASKET_MESSAGE = (By.XPATH, "//*[text()[contains(.,'added to your basket.')]]")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "h1~p:nth-child(2)")
    BASKET_PRICE = (By.XPATH, "//*[text()[contains(.,'Your basket total is now')]]/strong")



