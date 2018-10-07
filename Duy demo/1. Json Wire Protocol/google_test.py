from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.maximize_window()
driver.get('http://www.google.com')
element = driver.find_element(By.NAME, 'q')
driver.quit()
