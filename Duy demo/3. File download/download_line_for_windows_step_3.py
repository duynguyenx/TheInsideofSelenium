from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from hamcrest import assert_that, equal_to
import requests
from pathlib import Path
import hashlib


def file_as_bytes(file):
    with file:
        return file.read()

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

# Download file and check if file exist after downloaded
open('LineInst.exe', 'wb').write(response.content)
installation_file = Path("/home/duynguyenx/Desktop/Selenium_inside/Duy demo/3. File download/LineInst.exe")
assert_that(installation_file.is_file(), equal_to(True), 'Verify if the installation file is exist')

# Assert Hash string to check if the downloaded file is the correct one
assert_that(hashlib.md5(file_as_bytes(open('LineInst.exe', 'rb'))).hexdigest(), equal_to('b680228ffb3be773823e385b10e18ede'),
            'Verify if the installation file is correct')

driver.quit()
