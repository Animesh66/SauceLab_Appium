from Pages.BasePage import BasePage


class SecurityPinPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def type_pin(self, pin):
        self.click("enter_pin_id")
        self.type("enter_pin_id", pin)

