from pageobjects.basepage import BasePage
from conf.constants import LOCATOR


class HomePage(BasePage):

    def get_profile_name(self):
        return self.get_element_text(LOCATOR['PROFILE_NAME'])
