from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class SearchResultPage(BasePage):
    SECOND_PAGE_BUTTON = (By.CSS_SELECTOR, 'a[aria-label="2 sayfasına git"]')

    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')

    PRODUCT_LINK = (By.CSS_SELECTOR, 'div[data-index="9"] h2 a')

    # THIRD_PRODUCT = (By.CSS_SELECTOR, 'div[data-index="9"] h2 a')
    # THIRD_PRODUCT = (By.XPATH, '//div[@data-index="9"]//h2/a')
    # THIRD_PRODUCT = (By.CSS_SELECTOR, 'div[cel_widget_id="MAIN-SEARCH_RESULTS-9"] h2 a')
    # THIRD_PRODUCT = (By.XPATH, '//div[contains(@cel_widget_id, "MAIN-SEARCH_RESULTS")]/descendant::h2/a')
    # THIRD_PRODUCT = (By.CSS_SELECTOR, '[data-index="9"] .a-section.aok-relative.s-image-square-aspect')
    THIRD_PRODUCT = (By.CSS_SELECTOR, '[data-index="5"] .a-link-normal.s-line-clamp-4.s-link-style.a-text-normal')
    # RESULT_INFO = (By.CLASS_NAME, 'a-size-base a-spacing-small a-spacing-top-small a-text-normal')
    RESULT_INFO = (By.CSS_SELECTOR, 'h2.a-size-base.a-spacing-small.a-spacing-top-small.a-text-normal')


    def check_result(self):
        try:

            result_element = self.find_element(*self.RESULT_INFO)
            result_text = result_element.text.strip()  # Extract text and remove extra spaces

            if "1-" in result_text:
                print(f"Results Found -> {result_text}")
            else:
                print(f"No Result Found -> {result_text}")

        except Exception as e:
            print(f"Error: Unable to locate the result text. {e}")


        # if "1-" in self.get_text(self.RESULT_INFO):
        #     print("There are results for the search.")
        # else:
        #     print("There are no results for the search.")



    def scroll_to_bottom(self):
        """Scroll down using the Page Down key"""
        body = self.driver.find_element(By.TAG_NAME, "body")
        for _ in range(11):  # Scroll multiple times to ensure we reach the bottom
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)

    def go_to_second_page(self):
        """Scrolls down using the Page Down key and continuously tries clicking the second-page button"""
        body = self.driver.find_element(By.TAG_NAME, "body")

        while True:  # Keep trying until the button is clicked
            try:
                # Try clicking the button
                second_page_button = self.wait.until(ec.element_to_be_clickable(self.SECOND_PAGE_BUTTON))
                second_page_button.click()
                print("Successfully clicked the second-page button")
                break  # Exit loop once clicked

            except (ElementClickInterceptedException, TimeoutException):
                print("Second page button not clickable yet, scrolling down...")
                body.send_keys(Keys.PAGE_DOWN)  # Scroll down
                time.sleep(0.5)  # Wait for elements to load

    def click_second_page_button(self):
        self.click_element(self.SECOND_PAGE_BUTTON)

    def check_second_page(self):
        try:

            result_element = self.find_element(*self.RESULT_INFO)
            result_text = result_element.text.strip()  # Extract text and remove extra spaces

            if "49-" in result_text:
                print(f"You are on the second page")
            else:
                print(f"You are not on the second page")

        except Exception as e:
            print(f"Error: Unable to locate the result text. {e}")

    def select_product(self):
        self.click_element(self.THIRD_PRODUCT)
        """Extracts the product link and navigates to the product page"""
        # product_element = self.wait.until(ec.presence_of_element_located(self.PRODUCT_LINK))  # Wait for the element
        # product_url = product_element.get_attribute("href")  # Extract the href link
        #
        # print(f"Navigating to product page: {product_url}")
        # self.driver.get(product_url)  # Open the product page



