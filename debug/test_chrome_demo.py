import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By


def test_demo():
    desired_caps = dict(

        deviceName="Samsung_Note_10",
        platformName="Android",
        browserName="Chrome",
        chromedriverExecutable=".\\Drivers\\Chrome_Driver\\chromedriver.exe"

    )
    appium_service = AppiumService()
    appium_service.start()  # Appium service started
    print(appium_service.is_running)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.get("https://google.com")
    driver.find_element(By.XPATH, "//*[@name='q']").send_keys("Hello Appium")
    print(driver.title)
    time.sleep(3)
    driver.quit()
    appium_service.stop()  # Appium Service Stopped
