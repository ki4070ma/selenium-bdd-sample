from selenium.webdriver.common.by import By


class SearchPageLocators(object):
    SEARCH_TEXT_BOX = (By.NAME, 'q')
    SEARCH_BUTTON = (By.NAME, 'btnK')


class SearchResultPageLocators(object):
    RESULT_TITLES = (By.CLASS_NAME, 'LC20lb')
