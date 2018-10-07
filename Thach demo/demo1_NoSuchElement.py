import unittest
from selenium import webdriver


class DemoNoSuchElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_example1(self):
        self.driver.get('http://the-internet.herokuapp.com/iframe')
        element = self.driver.find_element_by_css_selector('#tinymce')
        element.send_keys('selenium demo')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
