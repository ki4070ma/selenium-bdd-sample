
from features.pages.common.basepage import BasePage
from features.pages.locators import SearchResultPageLocators


class SearchResultPage(BasePage):

    def __init__(self, driver):
        super(SearchResultPage, self).__init__(driver)

    def result_titles(self):
        return [el.text for el in self._results()]

    def _results(self):
        return self.driver.find_elements(*SearchResultPageLocators.RESULT_TITLES)
