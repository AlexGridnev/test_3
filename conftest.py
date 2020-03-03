import pytest
from selenium import webdriver

@pytest.fixture
def browser_is_opened():
    driver = webdriver.Chrome()
    yield driver
    driver.close()