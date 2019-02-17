#!/usr/bin/python3

import os
import unittest
from selenium import webdriver

from pages.google.search import SearchPage

class GoogleSearchPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'))

    def tearDown(self):
        import time
        time.sleep(3)  # Just to check the view on browse by me
        self.driver.close()

    def test_scenario1_search_keyword(self):
        search_page = SearchPage(self.driver)
        search_page.input_keyword('hogehoge')
        assert search_page.get_input_keyword() == 'hogehoge'


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(GoogleSearchPageTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
