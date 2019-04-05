import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class MainPage(BasePage):

    page_url = "https://www.centralpoint.nl"
    searchField = (By.XPATH, "//header/div[@class='container']//input[@name='search']")
    searchBtn = (By.XPATH, "//header/div[@class='container']//button")
    viewModeListButton = (By.XPATH, "//li[@data-viewmode='list']")
    productListLandscape = "//div[@class='card landscape wide']"

    def open(self):
        self.driver.get(self.page_url)
        self.driver.maximize_window()

    def fill_search_field(self, text):
        input_search = self.driver.find_element(*self.searchField)
        input_search.clear()
        input_search.send_keys(text)

    def click_search_btn(self):
        button = self.driver.find_element(*self.searchBtn)
        button.click()

    def search_product(self, text):
        self.fill_search_field(text)
        self.click_search_btn()
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.url_changes)

    def switch_to_list_view(self):
        button = self.driver.find_element(*self.viewModeListButton)
        button.click()

    def select_product_in_list(self, index):
        item = self.productListLandscape + "[" + str(index) + "]//div[@class='title']/a"
        product_title_locator = (By.XPATH, item)
        product = self.driver.find_element(*product_title_locator)
        product.location_once_scrolled_into_view
        time.sleep(1)
        product.click()
