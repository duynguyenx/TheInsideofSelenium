from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf import constants


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def type_text(self, tuple_selector, value, timeout=constants.SELENIUM_TIMEOUT_SECONDS):
        elem = self.wait_for_visibility_of_element(tuple_selector, timeout)
        elem.send_keys(value)

    def get_element_text(self, tuple_selector, timeout=constants.SELENIUM_TIMEOUT_SECONDS):
        element = self.wait_for_visibility_of_element(tuple_selector, timeout)
        return element.text

    def click_element(self,tuple_selector, timeout=constants.SELENIUM_TIMEOUT_SECONDS):
        elem = self.wait_for_element_to_be_clickable(tuple_selector, timeout)
        elem.click()

    def wait_for_visibility_of_element(self, tuple_selector, timeout=constants.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(tuple_selector))

    def wait_for_invisibility_of_element_located(self, tuple_selector, timeout=constants.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element_located(tuple_selector))

    def wait_for_element_to_be_clickable(self, tuple_selector, timeout=constants.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(tuple_selector))
