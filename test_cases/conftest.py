import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(params=["device1", "device2"], scope="function")
def appium_driver(request):
    appium_service = AppiumService()
    appium_service.start()
    print(appium_service.is_running)
    if request.param == "device1":
        desired_caps = dict(

            deviceName="Nexus 5",
            platformName="Android",
            appPackage="org.simple.clinic.staging",
            appActivity="org.simple.clinic.setup.SetupActivity",
            udid="emulator-5554"

        )
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    elif request.param == "device2":
        desired_caps = dict(

            deviceName="Pixel 4",
            platformName="Android",
            appPackage="org.simple.clinic.staging",
            appActivity="org.simple.clinic.setup.SetupActivity",
            udid="emulator-5556"

        )
        driver = webdriver.Remote('http://localhost:4724/wd/hub', desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    appium_service.stop()
    print(appium_service.is_running)


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
