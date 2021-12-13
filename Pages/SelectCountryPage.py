from Pages.BasePage import BasePage
from Pages.SelectClinicPage import SelectClinic


class NavigateCountry(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def select_country(self):
        self.click("select_country_radio_xpath")
        return SelectClinic(self.driver)
