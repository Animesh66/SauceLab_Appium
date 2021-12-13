import pytest


@pytest.mark.flaky(reruns=3)  # this wil rerun the failed test case 3 times
@pytest.mark.usefixtures("log_on_failure", "appium_driver")
class BaseTest:
    pass
