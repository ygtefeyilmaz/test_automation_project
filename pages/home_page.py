from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    ACCEPT_COOKIE = (By.ID, 'sp-cc-accept')
    HOMEPAGE_IDENTIFIER = (By.ID, "ad-topper-see-more")
    product_name = "samsung"


    def click_search_button(self):
        self.click_element(self.SEARCH_BUTTON)

    def accept_cookies(self):
        self.click_element(self.ACCEPT_COOKIE)

    def search_product(self):
     self.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(self.product_name)

    # def is_on_homepage(self):
    #      """Verifies if the current page is the homepage by checking the presence of a specific element."""
    #      try:
    #          self.wait.until(ec.presence_of_element_located(self.HOMEPAGE_IDENTIFIER))
    #          print("You are on the homepage.")
    #          return True
    #      except:
    #          print("You are NOT on the homepage.")
    #          return False
    def is_on_homepage(self):
        """Verifies that we are on the homepage by checking if the identifier present."""
        return self.assert_element_present(*self.HOMEPAGE_IDENTIFIER, error_message="Not on the homepage!", )

