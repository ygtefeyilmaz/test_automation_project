from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CategoryPage(BasePage):
    KAZAK_BREADCRUMB = (By.LINK_TEXT, "Erkek Kazak")
    QUICKFILTER_NEW = (By.CLASS_NAME, 'quick-filters__item--newest')
    PRODUCT_IMAGE = (By.CSS_SELECTOR, '.product-card:nth-of-type(2)')
    sub_category = 'Kazak'

    def get_breadcrumb_text(self):
        return self.get_text(self.KAZAK_BREADCRUMB)

    def click_quick_filter(self):
        self.click_element(*self.QUICKFILTER_NEW)

    def click_product(self):
        self.click_element(*self.PRODUCT_IMAGE)

