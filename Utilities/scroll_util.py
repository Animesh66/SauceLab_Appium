class ScrollUtil:

    @staticmethod
    def scroll_to_text(text,driver):
        driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance("
                                                   "0)).scrollIntoView(new UiSelector().textContains(\""+text+"\").instance(0))").click()

    @staticmethod
    def swipe_up(swipe_count,driver):
        for i in range(1,swipe_count +1):
            driver.swipe(514, 600, 514, 200, 1000)

    @staticmethod
    def swipe_down(swipe_count,driver):
        for i in range(1, swipe_count + 1):
            driver.swipe(514, 500, 514, 800, 1000)

    @staticmethod
    def swipe_left(swipe_count,driver):
        for i in range(1, swipe_count + 1):
            driver.swipe(900, 600, 200, 600, 1000)

    @staticmethod
    def swipe_right(swipe_count,driver):
        for i in range(1, swipe_count + 1):
            driver.swipe(200, 600, 900, 600, 1000)