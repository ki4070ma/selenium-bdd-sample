#!/usr/bin/python3

import os
from selenium import webdriver

from pages.google.search import SearchPage

def test_google():
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'))
    search_page = SearchPage(driver)
    search_page.input_keyword('hogehoge')
    assert search_page.get_input_keyword() == 'hogehoge'
    import time
    time.sleep(3)
    driver.close()

if __name__ == "__main__":
    test_google()
