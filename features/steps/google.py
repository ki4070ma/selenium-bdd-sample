from behave import *

@when('we visit google')
def step(context):
    pass
    # context.browser.get('http://www.google.com')

@then('it should have a title "Google"')
def step(context):
    pass
   # assert context.browser.title == "Google"

@when('we input "hogehoge" to text box at search page')
def step(context):
    context.search_page.input_keyword('hogehoge')

@then('it should have "hogehoge" at text box')
def step(context):
    assert context.search_page.get_input_keyword() == 'hogehoge'

