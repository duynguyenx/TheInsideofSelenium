import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Test3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_google_example(self):
        self.driver.get('http://www.github.com')
        element = self.driver.find_element_by_xpath('//input[@name="q"]')
        element.send_keys("Hello")
        element.send_keys(Keys.ENTER)
        element.clear()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
