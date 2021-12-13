import os
import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver(request):
    user_name = os.getenv("SAUCE_USERNAME")
    access_key = os.getenv("SAUCE_ACCESS_KEY")
    sauce_url = "https://{}:{}@ondemand.eu-central-1.saucelabs.com:443/wd/hub".format(user_name, access_key)
    sauce_options = {
        'name': request.node.name,
        'capturePerformance': True,
        'extendedDebugging': True
    }
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['appium:app'] = 'storage:filename=Simple_Demo.apk'
    desired_caps['appium:deviceName'] = 'Google Pixel 3a GoogleAPI Emulator'
    desired_caps['appium:platformVersion'] = '11.0'
    desired_caps['sauce:options'] = sauce_options
    desired_caps['sauce:options']['appiumVersion'] = '1.20.2'
    driver = webdriver.Remote(sauce_url, desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.start_activity('org.simple.clinic.staging', 'org.simple.clinic.setup.SetupActivity')
    yield driver
    driver.execute_script("sauce:job-result=passed")
    driver.quit()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
