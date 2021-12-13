from Pages.BasePage import BasePage
from Pages.SelectCountryPage import NavigateCountry


class GettingStartedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_get_started(self):
        self.click("get_started_button_xpath")
        return NavigateCountry(self.driver)