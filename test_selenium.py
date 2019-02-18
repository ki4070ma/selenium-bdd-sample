#!/usr/bin/python3

import os
import time
import unittest
from selenium import webdriver

from features.pages.google.search import SearchPage


class GoogleSearchPageTest(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options,
                                       executable_path=os.environ.get('CHROMEDRIVER_PATH'))

    def tearDown(self):
        time.sleep(1)  # Just to check the view on browse by me
        self.driver.quit()

    def test_scenario1_search_keyword(self):
        search_page = SearchPage(self.driver)
        search_page.input_keyword('hogehoge')
        assert search_page.search_query_word == 'hogehoge'

    def test_static_contents(self):
        search_page = SearchPage(self.driver)
        assert self.driver.title == 'Google'  # TODO Didn't use search_page instance


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(GoogleSearchPageTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
