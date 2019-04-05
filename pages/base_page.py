import time
from selenium.webdriver.common.by import By


class BasePage(object):
    """Base class to initialize the base page that will be called from all page"""

    def __init__(self, driver):
        self.driver = driver

    cookieAcceptBtn = (By.XPATH, '//a[@id="CybotCookiebotDialogBodyLevelButtonAccept"]')

    def accept_cookie(self):
        btn = self.driver.find_element(*self.cookieAcceptBtn)
        btn.click()

    def save_screenshot(self, path):
        timestamp = str(time.time())
        self.driver.get_screenshot_as_file("..\\screenshots\\" + timestamp + ".png")
