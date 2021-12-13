from Pages.InitialScreen import InitialScreen
from test_cases.BaseTest import BaseTest
import pytest
from Utilities.data_provider import get_data


class TestVerifyPhoneNo(BaseTest):

    @pytest.mark.parametrize("phone_number", get_data("verify_phone"))
    def test_verify_phone_no(self, phone_number):
        page = InitialScreen(self.driver)
        page.click_next().click_get_started().select_country().navigate_clinic().enter_phone_no(phone_number)
