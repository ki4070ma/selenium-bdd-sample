
from selenium.webdriver.common.keys import Keys

from features.pages.common.basepage import BasePage
from features.pages.google.search_result import SearchResultPage
from features.pages.locators import SearchPageLocators


class SearchPage(BasePage):

    def __init__(self, driver):
        super(SearchPage, self).__init__(driver)
        # self.driver.get('http://www.google.com')
        self.driver.get('https://www.google.com/?gl=us&hl=en&pws=0&gws_rd=cr')  # Google US

    def input_keyword(self, word):
        el = self._search_text_box()
        el.clear()
        el.send_keys(word)

    def search(self, word):
        el = self._search_text_box()
        el.clear()
        el.send_keys(word)
        el.send_keys(Keys.RETURN)
        # self._search_btn().click()/perform() TODO Need to check why this doesn't work
        return SearchResultPage(self.driver)

    @property
    def search_query_word(self):
        return self._search_text_box().get_attribute('value')

    def _search_text_box(self):
        return self.driver.find_element(*SearchPageLocators.SEARCH_TEXT_BOX)

    def _search_btn(self):
        return self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON)
