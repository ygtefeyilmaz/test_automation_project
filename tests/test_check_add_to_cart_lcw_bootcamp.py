import time

from selenium.webdriver.common.by import By

from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.search_result_page import SearchResultPage
from tests.base_test import BaseTest


class TestCheckAddToCartLcwBootcamp(BaseTest):

    def compare_product_names(name1, name2, word_count=3):
        """Compares the first few words of two product names."""
        short_name1 = " ".join(name1.split()[:word_count])  # Get first few words
        short_name2 = " ".join(name2.split()[:word_count])  # Get first few words

        assert short_name1 == short_name2, \
            f"❌ Test Failed: Expected '{short_name1}', but found '{short_name2}'"

        print(f"✅ Test Passed: Product matched -> '{short_name1}'")

    def test_check_lcw_add_to_cart(self):
        # time.sleep(2)

        home_page = HomePage(self.driver)
        home_page.accept_cookies()
        time.sleep(1)
        home_page.is_on_homepage()
        home_page.search_product()
        time.sleep(1)
        home_page.click_search_button()
        time.sleep(1)

        search_result_page = SearchResultPage(self.driver)
        time.sleep(2)
        search_result_page.check_result()
        time.sleep(2)
        search_result_page.go_to_second_page()
        time.sleep(2)
        search_result_page.check_second_page()
      #  search_result_page.scroll_to_bottom()
        time.sleep(3)
       # search_result_page.click_second_page_button()
        search_result_page.select_product()
        time.sleep(2)

        product_page = ProductPage(self.driver)
        time.sleep(2)
        expected_product_name = product_page.get_product_name()
        product_page.click_add_to_cart_button()
        time.sleep(2)
        product_page.click_cart_icon()

        cart_page = CartPage(self.driver)
        assert cart_page.is_cart_page(), "Test Failed: Not on the cart page"
        time.sleep(2)

        assert cart_page.is_correct_product_in_cart(expected_product_name), "Test Failed: Wrong product in the cart!"
        cart_page.click_delete_button()
        time.sleep(2)
        cart_page.click_main_logo()
        time.sleep(2)
        home_page.is_on_homepage()



        # home_page = HomePage(self.driver)
        # self.assertEqual(self.base_url, home_page.get_current_url(), 'lcw anasayfasında değilsin')
        # home_page.hover_category_erkek()
        # home_page.click_sub_category()
        #
        # category_page = CategoryPage(self.driver)
        # self.assertIn(category_page.sub_category, category_page.get_breadcrumb_text(), 'kazak kategorisinde değilsin')
        # category_page.click_quick_filter()
        # time.sleep(10)
        # category_page.click_product()
        #
        # product_page = ProductPage(self.driver)
        # self.assertTrue(product_page.is_add_to_cart_present(), 'product sayfasında değilsin')
        # product_page.click_beden_secenekleri()
        # product_page.click_add_to_cart_button()
        # self.assertEqual(product_page.cart_count, product_page.is_product_added(), 'sepete urun eksik ya da eklenemedi')
        # product_page.click_cart_icon()
        #
        # cart_page = CartPage(self.driver)
        # self.assertIn(cart_page.cart_header, cart_page.is_cart_header_present(), 'Cart Pagede degilsin')
        # cart_page.click_main_header_logo()