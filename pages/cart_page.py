from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[data-action="delete"][data-feature-id="delete"] input[data-action="delete"]')
    CART_HEADER = (By.CLASS_NAME, 'cart-header')
    MAIN_LOGO = (By.ID, 'nav-logo-sprites')
    CART_PAGE_IDENTIFIER = (By.ID, "sc-active-cart")  # Unique cart page element
    CART_PRODUCT_TITLE = (By.CLASS_NAME, "a-truncate-cut")  # Product name in cart
    DELETE_CONFIRMATION_MESSAGE = (By.CLASS_NAME, "sc-list-item-removed-msg")  # Message displayed after deletion

    def is_cart_header_present(self):
        return  self.get_text(self.CART_HEADER)

    def click_main_logo(self):
        self.click_element(self.MAIN_LOGO)

    def click_delete_button(self):
        self.click_element(self.DELETE_BUTTON)

    def is_cart_page(self):
        """Verifies that we are on the cart page."""
        return self.assert_element_present(*self.CART_PAGE_IDENTIFIER, error_message="Not on the cart page!")

    def get_product_name_in_cart(self):
        """Fetches the product name from the cart."""
        cart_product_element = self.wait.until(
            lambda driver: driver.find_element(*self.CART_PRODUCT_TITLE)
        )
        cart_product_name = cart_product_element.text.strip()
        print(f"Product Name in Cart: {cart_product_name}")  # Debugging log
        return cart_product_name

    def is_correct_product_in_cart(self, expected_product_name):
        """Verifies that the correct product is in the cart by checking the first few words."""
        cart_product_element = self.wait.until(
            lambda driver: driver.find_element(*self.CART_PRODUCT_TITLE)
        )

        full_cart_product_name = cart_product_element.text.strip()
        short_cart_product_name = " ".join(cart_product_element.text.strip().split()[:3])  # Extract first few words

        assert expected_product_name == short_cart_product_name, \
            f"Test Failed: Expected '{expected_product_name}', but found '{short_cart_product_name}'"

        print(f"Test Passed: Correct product is in the cart -> '{short_cart_product_name}'")
        return True

    def is_product_deleted(self):
        """Verifies that the product is removed from the cart by checking for the confirmation message."""
        try:
            confirmation_message = self.wait.until(
                lambda driver: driver.find_element(*self.DELETE_CONFIRMATION_MESSAGE)
            )
            assert confirmation_message.is_displayed(), "Product deletion message not found!"
            print("Product successfully removed from the cart.")
            return True
        except:
            print("Product deletion verification failed.")
            return False