
from features.pages.common.basepage import BasePage

class SearchPage(BasePage):

    def __init__(self, driver):
        super(SearchPage, self).__init__(driver)
        self.driver.get('http://www.google.com')

    def input_keyword(self, word):
        el = self._search_text_box()
        el.clear()
        el.send_keys(word)

    def get_input_keyword(self):
        el = self._search_text_box()
        return el.get_attribute('value')

    def _search_text_box(self):
        return self.driver.find_element_by_name('q')
