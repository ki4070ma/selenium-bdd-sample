# Readme
* To learn selenium

# What to be checked
## Static contents
* Covered all elements in locators.py

## User scenario
* Covered user stories

# Developments
## How to run
* Via behave(Main)

```bash
$ behave
```

* Via pytest(Just for test)

```bash
$ pytest
```

## Run flake8

```bash
$ flake8 --config=.config-flake8 .
```

## Dependencies
* [pip]: selenium, pytest, behave, flake8

# Checked items
* Test Design Considerations@SeleniumHQ
   * https://www.seleniumhq.org/docs/06_test_design_considerations.jsp 
* Test Automation Patterns Wiki
   * https://testautomationpatterns.org/wiki/index.php/Main_Page
   * [Japanese translation] just checked overview
      * http://blog.amateur-factory.jp/?eid=1444184

# Appium experiences
* Created test scenarios on 3rd party Android app
   * Page Object Pattern
   * Took evidence screen record, screen short just before action, adb log
* Tried BDD framework (behave by python)
   * https://github.com/behave/behave
