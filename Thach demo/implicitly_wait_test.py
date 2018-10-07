import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from conf.constants import LINKEDIN_ACCOUNT


class DemoExamples2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_linkedin_profile(self):
        self.driver.get("https://www.linkedin.com/")
        start_time = time.time()
        login_username = self.driver.find_element(By.CLASS_NAME, 'login-email')
        login_username.send_keys(LINKEDIN_ACCOUNT['Thach Hoang']['USER_NAME'])
        print("End test")
        print(time.time()-start_time)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
