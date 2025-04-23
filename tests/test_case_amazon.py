import time

from selenium.webdriver.common.by import By

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.search_result_page import SearchResultPage
from tests.base_test import BaseTest


class TestCaseAmazon(BaseTest):


    def test_case_amazon(self):
        # time.sleep(2)

        home_page = HomePage(self.driver)
        home_page.accept_cookies()
        time.sleep(1)
        home_page.search_product()
        # time.sleep(1)
        home_page.is_on_homepage()
        home_page.click_search_button()
        # time.sleep(1)

        search_result_page = SearchResultPage(self.driver)
        # time.sleep(2)
        search_result_page.check_result()
        # time.sleep(2)
        search_result_page.go_to_second_page()
        time.sleep(1)
        search_result_page.check_second_page()
        # time.sleep(3)
        search_result_page.select_product()
        # time.sleep(2)

        product_page = ProductPage(self.driver)
        # time.sleep(2)
        product_page.is_product_page()
        expected_product_name = product_page.get_product_name()
        product_page.click_add_to_cart_button()
        product_page.is_product_added_to_cart()
        # time.sleep(2)
        product_page.click_cart_icon()

        cart_page = CartPage(self.driver)
        assert cart_page.is_cart_page(), "Test Failed: Not on the cart page"
        # time.sleep(2)
        assert cart_page.is_correct_product_in_cart(expected_product_name), "Test Failed: Wrong product in the cart!"
        cart_page.click_delete_button()
        # time.sleep(2)
        assert cart_page.is_product_deleted(), "Test Failed: Product was not deleted from the cart!"
        # time.sleep(2)
        cart_page.click_main_logo()
        # time.sleep(2)
        home_page.is_on_homepage()
