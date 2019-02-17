import os
from selenium import webdriver

from features.pages.google.search import SearchPage

def before_all(context):
    print("Before all\n")
    context.browser = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'))
    context.search_page = SearchPage(context.browser)
