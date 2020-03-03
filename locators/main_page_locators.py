from selenium.webdriver.common.by import By


class MainPageLocators:
    def __init__(self):
        self.SEARCH_INPUT = (By.NAME, "q")
        self.DONATE_BUTTON = (By.CLASS_NAME, "donate-button")