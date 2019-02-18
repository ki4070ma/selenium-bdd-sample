from behave import *


@when('we input "{text}" to text box at search page')
def step(context, text):
    context.search_page.input_keyword(text)


@then('it should have "{text}" at text box')
def step(context, text):
    assert context.search_page.search_query_word == text


@when('we search with "{text}" as query at search page')
def step(context, text):
    context.search_result_page = context.search_page.search(text)


@then('Result page should have "{text}" at the top of results')
def step(context, text):
    assert context.search_result_page.result_titles()[0] == text
