import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class BaseTest(unittest.TestCase):
    base_url = 'https://www.amazon.com.tr/'

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.amazon.com.tr/')
        self.driver.implicitly_wait(5)


    def tearDown(self):
        self.driver.quit()
