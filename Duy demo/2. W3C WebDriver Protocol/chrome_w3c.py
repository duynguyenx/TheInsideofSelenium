from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

chrome_option = ChromeOptions()
chrome_option.add_experimental_option('w3c', True)
driver = Chrome(options=chrome_option)
driver.get('http://www.google.com')
element = driver.find_element(By.NAME, 'q')
driver.quit()
