from test_cases.BaseTest import BaseTest
import pytest


class TestMyDemoSauce(BaseTest):

    @pytest.mark.sanity
    def test_demo_sauce_app(self):
        assert True
