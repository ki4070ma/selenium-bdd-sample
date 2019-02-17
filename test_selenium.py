#!/usr/bin/python3

import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import requests

# class GetRoot(unittest.TestCase):
#     options = Options()
#     options.add_argument('--headless')
#     driver = webdriver.Chrome(chrome_options=options)
#
#     @classmethod
#     def setUpClass(cls):
#         cls.base_url = "https://www.seleniumhq.org/"
#         cls.driver.implicitly_wait(30)
#         cls.verificationErrors = []
#         cls.accept_next_alert = True
#         cls.driver.get(cls.base_url)
#
#     @pytest.mark.parametrize()
#     def test_get_page(self):
#         driver = self.driver
#         r = requests.get(driver.current_url)
#         self.assertEqual(r.status_code, 200)
#         title_target = "Selenium - Web Browser Automation"
#         print(driver.title)
#         self.assertEqual(title_target, driver.title)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()


def test_google():
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'))
    driver.get('http://www.google.com')
    elm = driver.find_element_by_name('q')
    elm.clear()
    elm.send_keys('hogehoge')
    assert elm.get_attribute('value') == 'hogehoge'
    import time
    time.sleep(3)
    driver.close()

if __name__ == "__main__":
    # unittest.main()
    test_google()