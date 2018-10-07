from pageobjects.basepage import BasePage
from conf.constants import LOCATOR


class SignIn(BasePage):

    def enter_user_name(self, value):
        self.type_text(LOCATOR['USER_NAME_BOX'], value)

    def enter_user_password(self, value):
        self.type_text(LOCATOR['PASSWORD_BOX'], value)

    def click_sign_in_button(self):
        self.click_element(LOCATOR['SIGN_IN_BTN'])
