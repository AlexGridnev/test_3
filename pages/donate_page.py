from locators.donate_page_locators import DonatePageLocators 
from selenium.webdriver.support import expected_conditions

class DonatePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait 
        self.locators = DonatePageLocators()

    def check_donate_button_exists(self):
        element = self.wait.until(expected_conditions.presence_of_element_located(self.locators.DONATE_BUTTON))
        return element is not None