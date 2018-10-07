from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

driver = Firefox()
driver.get('http://www.google.com')
element = driver.find_element(By.NAME, 'q')
driver.quit()
