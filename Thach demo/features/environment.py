from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def before_all(context):

    ff_options = Options()
    ff_options.add_argument('disable-infobars')
    ff_options.add_argument("--start-maximized")
    context.driver = webdriver.Firefox(executable_path=r'/home/duynguyenx/Desktop/Selenium_inside/geckodriver.exe', options=ff_options)
    context.driver.implicitly_wait(10)


def after_all(context):
    context.driver.quit()
