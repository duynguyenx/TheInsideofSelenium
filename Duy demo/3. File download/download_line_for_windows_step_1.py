from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from hamcrest import assert_that, equal_to
import requests

driver = Chrome()
driver.maximize_window()
driver.get('https://line.me/vi/download')
download_button_element = driver.find_element(By.ID, 'winDownload')
download_url = download_button_element.get_attribute('href')

# Assert the download url
assert_that(download_url, equal_to('https://scdn.line-apps.com/client/win/new/LineInst.exe'),
            'Verify the download url is correct')

# Assert the download link is alive
response = requests.get(download_url, allow_redirects=True)
assert_that(response.status_code, equal_to(200), 'Verify if response status code is 200')

driver.quit()
