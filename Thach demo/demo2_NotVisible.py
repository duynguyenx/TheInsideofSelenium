import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestNotVisible(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_not_visible(self):
        self.driver.get('https://letskodeit.teachable.com/p/practice/')
        self.driver.find_element(By.ID, 'hide-textbox').click()
        self.driver.find_element(By.ID, 'displayed-text').send_keys('Selenium Demo')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
