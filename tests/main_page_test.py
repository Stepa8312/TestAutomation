import unittest
from pages.pages import Pages
from environment_setup import EnvironmentSetup


class MainPageTests(EnvironmentSetup):

    def test_search_product(self):
        page = Pages(self.driver)
        page.main_page.open()
        page.main_page.accept_cookie()
        page.main_page.search_product('laptop')
        page.main_page.switch_to_list_view()
        page.main_page.select_product_in_list(3)
        page.main_page.save_screenshot()
