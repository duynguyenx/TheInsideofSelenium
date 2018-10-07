from selenium.webdriver.common.by import By

LINKEDIN_ACCOUNT = {
    'Thach Hoang': {
        'USER_NAME': 'your_user_name',
        'PASSWORD': 'your_password'
    },
}

SITE = 'https://www.linkedin.com'
SELENIUM_TIMEOUT_SECONDS = 15


LOCATOR = {
    'USER_NAME_BOX': (By.CLASS_NAME, 'login-email'),
    'PASSWORD_BOX': (By.CLASS_NAME, 'login-password'),
    'SIGN_IN_BTN': (By.ID, 'login-submit'),
    'PROFILE_NAME': (By.CSS_SELECTOR, '[data-control-name="identity_welcome_message"]')
}