from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import create_message_internal


@given('The user has found the respondent they need to query data with')
def user_has_found_respondent():
    pass


@when("They choose to send them a secure message and navigated to the 'send message' page")
@given("The user is on the send message page")
def navigate_to_send_message():
    # TODO This must be updated when the method of passing respondent details is finalised

    create_message_internal.go_to(create_message_internal.found_respondent_details())


@then("The 'To' field is populated with the respondents name")
def check_to_field():
    # TODO This must be updated when the method of passing respondent details is finalised

    to_field = browser.find_by_id('to-label').first
    assert to_field == create_message_internal.found_respondent_details().get('to')


@when("They enter text in the subject of the message")
def user_enters_text_in_subject():
    pass


@when("They enter text in the body of the message")
def user_enters_text_in_message_body():
    pass


@then("They are able to enter free text up to and including 100 characters")
def user_able_to_enter_subject():
    pass


@then("They are able to enter free text up to and including 10,000 characters")
def user_able_to_enter_message_body():
    pass


@when("They enter text in the subject and body of the message")
def user_has_entered_text_in_subject_and_body():
    browser.find_by_id('secure-message-subject').clear()
    browser.find_by_id('secure-message-body').clear()
    browser.find_by_id('secure-message-subject').insert('Subject text')
    browser.find_by_id('secure-message-body').insert('Message text')


@then("They are able to send the message")
def user_is_able_to_send_message():
    create_message_internal.click_message_send_button()
    # TODO assert sending succeeds


@when("They choose to cancel out of sending a message")
def user_cancels_sending_message():
    create_message_internal.click_cancel_button()
