import unittest
from pages.pages import Pages
from environment_setup import EnvironmentSetup


class MainPageTests(EnvironmentSetup):

    def test_search_product(self):
        page = Pages(self.driver)
        page.main_page.open()
