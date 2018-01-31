from behave import given, when, then

from acceptance_tests.features.pages import sign_in_respondent
from acceptance_tests import browser
from config import Config


@given('the user is signed into their account')
def signed_in(context):
    sign_in_respondent.go_to()
    browser.driver.find_element_by_id('username').send_keys(Config.USERNAME)
    browser.driver.find_element_by_id('password').send_keys(Config.PASSWORD)
    browser.find_by_id('SIGN_IN_BUTTON').click()


@then('the user signs out')
def signed_out(context):
    browser.find_by_id('SIGN_OUT_BUTTON').click()
