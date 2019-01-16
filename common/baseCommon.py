from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
class BaseCommon():
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, para):
        return WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*para))

    def get_elements(self, para):
        return WebDriverWait(self.driver, 5).until(lambda x: x.find_elements(*para))

    def alert_accept(self):
        return self.driver.Alert.accept()