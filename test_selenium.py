#!/usr/bin/python3

import os
from selenium import webdriver

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
    test_google()
