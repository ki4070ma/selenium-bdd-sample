from features.pages.common.utils import take_screenshot


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        take_screenshot(self.driver)
