import unittest
from selenium.webdriver import ActionChains
from selenium import webdriver
import time


class TestNotViFsable3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_not_visable3(self):
        self.driver.get('http://manos.malihu.gr/repository/custom-scrollbar/demo/examples/complete_examples.html')
        time.sleep(5)
        element = self.driver.find_element_by_xpath(".//*[@id='mCSB_3_container']/p[9]/textarea")
        time.sleep(5)

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.send_keys('Selenium Demo')
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
