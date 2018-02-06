from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import create_message_internal


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
    create_message_internal.enter_text_in_message_subject('Message subject')


@when("They enter text in the body of the message")
def user_enters_text_in_message_body():
    create_message_internal.enter_text_in_message_body('Message body')


@then("They are able to enter free text up to and including 100 characters")
def user_able_to_enter_subject():
    create_message_internal.enter_text_in_message_subject('1' * 100)
    assert create_message_internal.message_subject_text() == '1' * 100

    create_message_internal.enter_text_in_message_subject('1' * 200)
    assert len(create_message_internal.message_subject_text()) <= 100


@then("They are able to enter free text up to and including 10,000 characters")
def user_able_to_enter_message_body():
    create_message_internal.enter_text_in_message_body('1' * 10000)
    assert create_message_internal.message_body_text() == '1' * 10000

    create_message_internal.enter_text_in_message_body('1' * 20000)
    assert len(create_message_internal.message_body_text()) <= 10000


@when("They enter text in the subject and body of the message")
@given("The user has entered text in the subject and body of the message")
def user_has_entered_text_in_subject_and_body():
    create_message_internal.enter_text_in_message_subject('Message subject')
    create_message_internal.enter_text_in_message_body('Message body')


@then("They are able to send the message")
@when("They select send")
def user_is_able_to_send_message():
    create_message_internal.click_message_send_button()
    # TODO assert that the sending succeeds


@when("They choose to cancel out of sending a message")
def user_cancels_sending_message():
    create_message_internal.click_cancel_button()


@then("They are navigated back to the page in which they navigated from")
def user_is_navigated_back():
    pass


@then("They are navigated to the inbox of messages")
@when("They are navigated to the inbox of messages")
def user_is_navigated_to_inbox():
    # TODO update with correct inbox url
    assert 'messages/inbox' in browser.url


@given("The user has sent a secure message")
def user_sent_secure_message():
    user_has_entered_text_in_subject_and_body()
    user_is_able_to_send_message()


@then("They are presented with confirmation that the message has been sent")
def user_is_given_message_sent_confirmation():
    browser.driver.find_element_by_id("message-sent-confirmation")
