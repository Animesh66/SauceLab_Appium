import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By


def test_demo():
    desired_caps = dict(

        deviceName="Samsung_Note_10",
        platformName="Android",
        appPackage="com.samsung.android.dialer",
        appActivity=".DialtactsActivity",
        udid="R58M86QW34P"

    )

    driver = webdriver.Remote('http://127.0.0.1:4724/wd/hub', desired_caps)
    driver.find_element(By.XPATH, "//android.widget.Button[@text='Continue']").click()
    driver.find_element(By.XPATH, "//android.widget.TextView[@text='Recents']").click()
