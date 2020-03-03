from pages.main_page import MainPage
from pages.donate_page import DonatePage 

def test_donate_page_button(browser_is_opened):
    main_page = MainPage(*browser_is_opened)
    main_page.click_donate_button()
    donate_page = DonatePage(*browser_is_opened)
    assert donate_page.check_donate_button_exists()