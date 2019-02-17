
from features.pages.common.basepage import BasePage
from features.pages.locators import SearchPageLocators


class SearchPage(BasePage):

    def __init__(self, driver):
        super(SearchPage, self).__init__(driver)
        self.driver.get('http://www.google.com')

    def input_keyword(self, word):
        el = self._search_text_box()
        el.clear()
        el.send_keys(word)

    @property
    def search_query_word(self):
        return self._search_text_box().get_attribute('value')

    def _search_text_box(self):
        print(*SearchPageLocators.SEARCH_TEXT_BOX)
        return self.driver.find_element(*SearchPageLocators.SEARCH_TEXT_BOX)
