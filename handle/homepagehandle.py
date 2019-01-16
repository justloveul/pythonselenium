from page.homepage import HomePage

class HomePageHandle:
    def __init__(self, driver):
        self.driver = driver
        self.homePage = HomePage(self.driver)

    def send_key(self, msg):
        self.homePage.get_search_element().clear()
        self.homePage.get_search_element().send_keys(msg)

    def click_button(self):
        self.homePage.get_button_element().click()