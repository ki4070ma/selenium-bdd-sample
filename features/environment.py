import os
from selenium import webdriver

from features.pages.google.search import SearchPage

def before_all(context):
    print("Before all")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    context.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=os.environ.get('CHROMEDRIVER_PATH'))
    context.search_page = SearchPage(context.browser)

def after_all(context):
    print("After all")
    import time
    time.sleep(3)  # Just to check the view on browse by me
    context.browser.quit()
