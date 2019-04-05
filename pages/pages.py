from selenium import webdriver
from pages.main_page import MainPage


class Pages:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver=self.driver)
