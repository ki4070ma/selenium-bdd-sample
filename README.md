[![Build Status](https://travis-ci.org/ki4070ma/selenium-sample.svg?branch=master)](https://travis-ci.org/ki4070ma/selenium-sample)

[![Job Status](https://inspecode.rocro.com/badges/github.com/ki4070ma/selenium-sample/status?token=_tZxm64lNuOvF2warut_6-UssHYB3IrGP5Z6qSlxQvc)](https://inspecode.rocro.com/jobs/github.com/ki4070ma/selenium-sample/latest?completed=true) [![Report](https://inspecode.rocro.com/badges/github.com/ki4070ma/selenium-sample/report?token=_tZxm64lNuOvF2warut_6-UssHYB3IrGP5Z6qSlxQvc&branch=master)](https://inspecode.rocro.com/reports/github.com/ki4070ma/selenium-sample/branch/master/summary)

[![Maintainability](https://api.codeclimate.com/v1/badges/18287c763cc9e86b0919/maintainability)](https://codeclimate.com/github/ki4070ma/selenium-sample/maintainability) 

# Readme
* To learn selenium

# What to be checked
## Static contents
* Covered all elements in locators.py

## User scenario
* Covered user stories

# Developments
## Setup

* ```brew instal allure```
* ```pip install -r developments.txt```
* ```pre-commit install```

## Run tests
* Via behave(Main)
   * Will be executed under features folder

```bash
$ python -m behave
$ python -m behave --no-capture (Output print statement in terminal)
$ python -m behave --tags=TAG (Run only tagged case)
```

* Via behave with allure

```bash
$ behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
$ allure serve %allure_result_folder%
```

* Via pytest(Just for test)
   * Will be executed test_selenium.py

```bash
$ python -m pytest
```

## Run autopep8

```bash
$ python -m autopep8 -r --global-config .config-pep8 -i .
```

# References
* Selenium official site
   * Webdriver API
      * https://selenium-python.readthedocs.io/api.html
   * Test Design Considerations@SeleniumHQ
      * https://www.seleniumhq.org/docs/06_test_design_considerations.jsp
* Test Automation Patterns Wiki
   * https://testautomationpatterns.org/wiki/index.php/Main_Page
   * [Japanese translation] just checked overview
      * http://blog.amateur-factory.jp/?eid=1444184
* Selenium by python
   * https://kurozumi.github.io/selenium-python/index.html
* Selenium/Appium Advent Calendar 2018
   * https://qiita.com/advent-calendar/2018/selenium_and_appium
* Selenium IDE
   * https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd/related
 
