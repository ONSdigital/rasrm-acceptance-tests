from behave import given, when, then

from acceptance_tests.features.pages import sign_in_respondent
from config import Config


@given('the user is signed into their account')
def signed_in(context):
    sign_in_respondent.goto()
    context.browser.find_by_id('username').send_keys(Config.USERNAME)
    context.browser.find_by_id('password').send_keys(Config.PASSWORD)
    context.browser.find_by_id('SIGN_IN_BUTTON').click()


@then('the user signs out')
def signed_out(context):
    context.browser.find_by_id('SIGN_OUT_BUTTON').click()
