import os
from selenium import webdriver

from features.pages.google.search import SearchPage
from features.pages.common.utils import GlobalVar

# Returns abs path relative to this file and not cwd


def PATH(p): return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def before_all(context):
    import datetime as dt
    GlobalVar().log_root_dir = os.path.join(PATH('.'), '..', 'output', dt.datetime.now().strftime('%y%m%d-%H%M%S'))
    os.path.isdir(GlobalVar().log_root_dir) or os.makedirs(GlobalVar().log_root_dir)


def before_scenario(context, scenario):
    GlobalVar().log_dir = os.path.join(GlobalVar().log_root_dir, scenario.name.replace(' ', ''))
    os.path.isdir(GlobalVar().log_dir) or os.makedirs(GlobalVar().log_dir)

    print("**Before scenario")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    context.browser = webdriver.Chrome(chrome_options=chrome_options,
                                       executable_path=os.environ.get('CHROMEDRIVER_PATH'))
    context.search_page = SearchPage(context.browser)


def after_scenario(context, scenario):
    print("**After scenario")
    import time
    time.sleep(1)  # Just to check the view on browse by me
    context.browser.quit()
