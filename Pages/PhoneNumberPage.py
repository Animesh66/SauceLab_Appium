from Pages.BasePage import BasePage
from Pages.RoleNamePage import RoleNamePage


class PhoneNumber(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_phone_no(self, number):
        self.click("enter_phone_no_id")
        self.type("enter_phone_no_id", number)

    def navigate_next(self):
        self.click("next_button_xpath")
        return RoleNamePage(self.driver)
