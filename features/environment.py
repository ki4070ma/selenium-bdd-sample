import os
from selenium import webdriver

from features.pages.common.utils import GlobalVar
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# Returns abs path relative to this file and not cwd


def PATH(p): return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def before_all(context):
    import datetime as dt
    GlobalVar().log_root_dir = os.path.join(PATH('.'), '..', 'output', dt.datetime.now().strftime('%y%m%d-%H%M%S'))
    os.path.isdir(GlobalVar().log_root_dir) or os.makedirs(GlobalVar().log_root_dir)


def before_scenario(context, scenario):
    GlobalVar().log_dir = os.path.join(GlobalVar().log_root_dir, scenario.name.replace(' ', '_'))
    os.path.isdir(GlobalVar().log_dir) or os.makedirs(GlobalVar().log_dir)

    print("**Before scenario")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    context.browser = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
    )
    # TODO Need to know difference between remote webdriver and local webdriver
    # context.browser = webdriver.Chrome(chrome_options=chrome_options,
    # executable_path=os.environ.get('CHROMEDRIVER_PATH'))


def after_scenario(context, scenario):
    print("**After scenario")
    import time
    time.sleep(1)  # Just to check the view on browse by me
    context.browser.quit()
