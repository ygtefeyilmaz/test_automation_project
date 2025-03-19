from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
from pages.base_page import BasePage


class ProductPage(BasePage):
    BEDEN_SECENEKLERI = (By.CSS_SELECTOR, '.option-box')
    ADD_TO_CART = (By.ID, 'add-to-cart-button')
    CART_ICON = (By.ID, 'nav-cart')
    CART_COUNT = (By.ID, 'nav-cart-count')
    PRODUCT_NAME = (By.ID, 'productTitle')  # Locator for 3rd product name
    ADD_CONFIRMATION_MESSAGE = (By.ID, "NATC_SMART_WAGON_CONF_MSG_SUCCESS")  # Message displayed after adding product


    def is_add_to_cart_present(self):
        return self.find(*self.ADD_TO_CART)

    def click_beden_secenekleri(self):
        self.click_element(*self.BEDEN_SECENEKLERI)

    def click_add_to_cart_button(self):
        self.click_element(self.ADD_TO_CART)

    def is_product_added(self):
        return self.get_text(self.CART_COUNT)

    def click_cart_icon(self):
        self.click_element(self.CART_ICON)

    # def get_product_name(self):
    #     """Fetches the name of the 3rd product before adding to cart."""
    #     product_element = self.wait.until(
    #         lambda driver: driver.find_element(*self.THIRD_PRODUCT_NAME)
    #     )
    #     product_name = product_element.text.strip()
    #     print(f"✅ 3rd Product Name: {product_name}")  # Debugging log
    #     return product_name

    # def get_product_name(self):
    #     """Fetches the product name from the product page."""
    #     product_element = self.wait.until(
    #         lambda driver: driver.find_element(*self.PRODUCT_NAME)
    #     )
    #     product_name = product_element.text.strip()
    #     print(f"✅ Product Name on Page: {product_name}")  # Debugging log
    #     return product_name

    def get_product_name(self, word_count=3):
        """Fetches the product name from the product page and returns the first few words."""
        product_element = self.wait.until(
            lambda driver: driver.find_element(*self.PRODUCT_NAME)
        )
        full_product_name = product_element.text.strip()
        short_product_name = " ".join(full_product_name.split()[:word_count])  # Extract first few words

        print(f"✅ Product Name on Page: {short_product_name}")  # Debugging log
        return short_product_name

    def is_product_added_to_cart(self):
        """Verifies that the product is added to the cart by checking for the confirmation message."""
        try:
            confirmation_message = self.wait.until(
                lambda driver: driver.find_element(*self.ADD_CONFIRMATION_MESSAGE)
            )
            assert confirmation_message.is_displayed(), "❌ Test Failed: Product addition message not found!"
            print("✅ Test Passed: Product successfully added to the cart.")
            return True
        except:
            print("❌ Test Failed: Product addition verification failed.")
            return False
