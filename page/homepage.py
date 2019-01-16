from page.basepage import BasePage
from selenium.webdriver.common.by import By
from public.getData import get_data

class HomePage(BasePage):

    def get_search_element(self):
        return super().get_element(get_data("search"))

    def get_button_element(self):
        return super().get_element(get_data("button"))