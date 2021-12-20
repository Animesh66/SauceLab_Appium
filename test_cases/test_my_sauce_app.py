from test_cases.BaseTest import BaseTest
import pytest


class TestMyDemoSauce(BaseTest):

    @pytest.mark.sanity
    def test_my_demo_sauce(self):
        assert True
