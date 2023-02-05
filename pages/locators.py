from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_TITLE = (By.XPATH, "//h1")
    PRICE = (By.CSS_SELECTOR, "p[class=price_color]")

    TITLE_AFTER_ADD = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE_AFTER_ADD = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
