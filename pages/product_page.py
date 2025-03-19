from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART = (By.ID, 'add-to-cart-button')
    BUY_NOW_BUTTON = (By.ID, 'buy-now-button')
    CART_ICON = (By.ID, 'nav-cart')
    CART_COUNT = (By.ID, 'nav-cart-count')
    PRODUCT_NAME = (By.ID, 'productTitle')  # Locator for product name
    ADD_CONFIRMATION_MESSAGE = (By.ID, "NATC_SMART_WAGON_CONF_MSG_SUCCESS")  # Message displayed after adding product

    def is_product_page(self):
        return self.assert_element_present(*self.BUY_NOW_BUTTON, error_message="Not on the Product page!")

    def is_add_to_cart_present(self):
        return self.find(*self.ADD_TO_CART)

    def click_add_to_cart_button(self):
        self.click_element(self.ADD_TO_CART)

    def is_product_added(self):
        return self.get_text(self.CART_COUNT)

    def click_cart_icon(self):
        self.click_element(self.CART_ICON)

    def get_product_name(self, word_count=3):
        """Fetches the product name from the product page and returns the first few words."""
        product_element = self.wait.until(
            lambda driver: driver.find_element(*self.PRODUCT_NAME)
        )
        full_product_name = product_element.text.strip()
        short_product_name = " ".join(full_product_name.split()[:word_count])  # Extract first few words

        print(f"Product Name on Page: {short_product_name}")
        return short_product_name

    def is_product_added_to_cart(self):
        """Verifies that the product is added to the cart by checking for the confirmation message displayed or not."""
        try:
            confirmation_message = self.wait.until(
                lambda driver: driver.find_element(*self.ADD_CONFIRMATION_MESSAGE)
            )
            assert confirmation_message.is_displayed(), "Product is not added to cart."
            print("Product successfully added to the cart.")
            return True
        except:
            print("Product addition verification failed.")
            return False
