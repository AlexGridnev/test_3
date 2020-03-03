class SearchResultsPage:
    def __init__(self, driver):
        self.page_source = driver.page_source

    def results_found(self):
        return "No results found." not in self.page_source