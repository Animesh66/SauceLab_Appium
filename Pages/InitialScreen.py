from Pages.BasePage import BasePage
from Pages.GettingStartedPage import GettingStartedPage


class InitialScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_next(self):
        self.click("next_button_xpath")
        # self.static_wait(3)
        return GettingStartedPage(self.driver)
