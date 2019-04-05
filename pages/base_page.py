from selenium.webdriver.common.by import By


class BasePage(object):
    """Base class to initialize the base page that will be called from all page"""

    def __init__(self, driver):
        self.driver = driver

    cookieAcceptBtn = (By.XPATH, '//a[@id="CybotCookiebotDialogBodyLevelButtonAccept"]')

    def accept_cookie(self):
        btn = self.driver.find_element(*self.cookieAcceptBtn)
        btn.click()
