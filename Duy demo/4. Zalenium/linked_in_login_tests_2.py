from selenium.webdriver import ChromeOptions
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from hamcrest import assert_that, equal_to
from config.constants import CREDENTIAL

chromeoption = ChromeOptions()
browser = Remote(command_executor="http://172.17.0.2:4445/wd/hub", options=chromeoption)

browser.implicitly_wait(7)
browser.maximize_window()
browser.get('http://linkedin.com')
browser.find_element(By.ID, 'login-email').send_keys(CREDENTIAL['user_name'])
browser.find_element(By.ID, 'login-password').send_keys(CREDENTIAL['password'])
browser.find_element(By.ID, 'login-submit').click()
actual_full_name = browser.find_element(By.CSS_SELECTOR, 'a[data-control-name="identity_welcome_message"]').text
expected_full_name = 'Duy Nguyen'

actual_position = browser.find_element(By.CSS_SELECTOR, '.identity-headline').text
expected_position = 'Principal Automation Test Engineer'

assert_that(actual_full_name, equal_to(expected_full_name), 'Verify full name')
assert_that(actual_position, equal_to(expected_position), 'Verify position')

browser.quit()
