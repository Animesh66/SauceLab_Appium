from Pages.BasePage import BasePage
from Pages.SecurityPinPage import SecurityPinPage


class RoleNamePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_role_name(self, role):
        self.click("full_name_id")
        self.type("full_name_id", role)
        self.hide_keyboard()
        self.click("next_button_xpath")
        return SecurityPinPage(self.driver)