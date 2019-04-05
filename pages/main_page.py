from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    page_url = "https://www.centralpoint.nl"
    search_field = (By.XPATH, "//header/div[@class='container']//input[@name='search']")
    search_btn = (By.XPATH, "//header/div[@class='container']//button")

    def open(self):
        self.driver.get(self.page_url)
        self.driver.maximize_window()
