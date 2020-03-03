from selenium.webdriver.common.keys import Keys
from locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://www.python.org")
        self.title = self.driver.title
        self.locators = MainPageLocators()

    def search_without_locator_deps(self, search_string):
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys(search_string)
        elem.send_keys(Keys.RETURN)

    def search(self, search_string):
        elem = self.driver.find_element(*self.locators.SEARCH_INPUT)
        elem.clear()
        elem.send_keys(search_string)
        elem.send_keys(Keys.RETURN)