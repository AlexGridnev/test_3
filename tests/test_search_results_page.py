from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage

def test_python_org_search(browser_is_opened):
    python_main_page = MainPage(*browser_is_opened)
    assert "Python" in python_main_page.title
    python_main_page.search("pycon")
    search_results_page = SearchResultsPage(*browser_is_opened)
    assert search_results_page.results_found()
