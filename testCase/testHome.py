import unittest, time
from selenium import webdriver
from handle.homepagehandle import HomePageHandle

class TestHome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.homepagehandle = HomePageHandle(self.driver)

    def test1(self):
        """搜索美女"""
        self.driver.get("http://www.baidu.com")
        time.sleep(2)
        self.homepagehandle.send_key("美女")
        time.sleep(2)
        self.homepagehandle.click_button()
        time.sleep(2)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()