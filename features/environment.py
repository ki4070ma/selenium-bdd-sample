import os
from selenium import webdriver

def before_feature(context, feature):
    print("Before feature\n")
    # context.browser = webdriver.Chrome()
    context.browser = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'))
