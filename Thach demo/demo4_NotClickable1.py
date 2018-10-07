import unittest
import time
from selenium import webdriver


class TestNotClickable(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test_not_clickable(self):
        self.driver.get('https://vietjetair.com/Sites/Web/vi-VN/Home')
        origin = self.driver.find_element_by_css_selector('#select2-selectOrigin-container')
        origin.click()
        time.sleep(3)
        elem = self.driver.find_element_by_css_selector('[name$="PromoCode"]')
        elem.click().send_keys('Selenium Demo')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
