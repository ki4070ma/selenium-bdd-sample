# Readme
* To learn selenium

# What to be checked
## Static contents
* Covered all elements in locators.py

## User scenario
* Covered user stories

# Developments
## How to run tests
* Via behave(Main)
   * Will be executed under features folder

```bash
$ behave
```

* Via pytest(Just for test)
   * Will be executed test_selenium.py

```bash
$ pytest
```

## Run autopep8

```bash
$ python -m autopep8 -r --global-config .config-pep8 -i .
```

## Dependencies
* [pip]: selenium, pytest, behave, autopep8

# References
* Test Design Considerations@SeleniumHQ
   * https://www.seleniumhq.org/docs/06_test_design_considerations.jsp 
* Test Automation Patterns Wiki
   * https://testautomationpatterns.org/wiki/index.php/Main_Page
   * [Japanese translation] just checked overview
      * http://blog.amateur-factory.jp/?eid=1444184
* Selenium by python
   * https://kurozumi.github.io/selenium-python/index.html
