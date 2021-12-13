from Pages.BasePage import BasePage


class LocationScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_skip(self):
        self.click("skip_button_xpath")