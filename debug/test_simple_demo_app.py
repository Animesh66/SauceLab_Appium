import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By


def test_simple_demo_app():
    desired_caps = dict(

        deviceName="Samsung_Note_10",
        platformName="Android",
        appPackage="org.simple.clinic.staging",
        appActivity="org.simple.clinic.setup.SetupActivity",
        udid="emulator-5554"

    )

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
