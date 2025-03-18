from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find(self, locator):
        return self.driver.find_element(locator)

    def find_element(self, by, value):
        """Waits for an element to be present and returns it"""
        return self.wait.until(ec.presence_of_element_located((by, value)))

    def find_element_clickable(self, by, value):
        """Waits for an element to be clickable and returns it"""
        return self.wait.until(ec.element_to_be_clickable((by, value)))

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def hover_element(self, locator):
        element = self.find(locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_current_url(self):
        return self.driver.current_url

    def wait_element(self, method, message=''):
        return self.wait.until(ec.element_to_be_clickable(method), message)

    def get_text(self, locator):
        return self.find_element(*locator).text

    def enter_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def click_element_with_scroll(self, by, value, max_scrolls=10):
        """Tries clicking an element. If not clickable, scrolls down iteratively until it succeeds."""
        body = self.driver.find_element("tag name", "body")

        for _ in range(max_scrolls):  # Try clicking multiple times while scrolling down
            try:
                element = self.find_element_clickable(by, value)
                element.click()
                print("Successfully clicked the element!")
                return  # Exit the function once clicked
            except:
                print("Element not clickable yet, scrolling down...")
                body.send_keys(Keys.PAGE_DOWN)  # Scroll down
                time.sleep(0.5)  # Wait for page to load

        raise Exception("Failed to click the element after scrolling down multiple times.")

    def assert_element_present(self, by, value, error_message="Element not found!"):
        """Asserts that an element is present on the page."""
        try:
            self.wait.until(ec.presence_of_element_located((by, value)))
            print(f"You are on the correct page")
            return True
        except:
            raise AssertionError(f"Test Failed: {error_message}")

    def compare_product_names(name1, name2, word_count=3):
        """Compares the first few words of two product names."""
        short_name1 = " ".join(name1.split()[:word_count])  # Get first few words
        short_name2 = " ".join(name2.split()[:word_count])  # Get first few words

        assert short_name1 == short_name2, \
            f"❌ Test Failed: Expected '{short_name1}', but found '{short_name2}'"

        print(f"✅ Test Passed: Product matched -> '{short_name1}'")
