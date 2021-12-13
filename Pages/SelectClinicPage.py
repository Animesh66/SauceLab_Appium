from Pages.BasePage import BasePage
from Pages.PhoneNumberPage import PhoneNumber


class SelectClinic(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_clinic(self):
        self.click("select_clinic_radio_xpath")
        return PhoneNumber(self.driver)
