from acceptance_tests import browser
from config import Config
from common.browser_utilities import wait_for_element_by_id


def go_to():
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/messages")


def go_to_thread():
    wait_for_element_by_id(element_id='message-link-1', timeout=20, retry=1)
    thread_subject = browser.find_by_id('message-link-1')
    thread_subject.click()


def count_thread_message():
    internals = browser.find_by_name('sm-from-ons')
    external = browser.find_by_name('sm-from-respondent')
    return len(internals) + len(external)


def is_conversation_with_sent_and_received_messages():
    internals = browser.find_by_name('sm-from-ons')

    # TODO Enable this when we are able to send message from Front-stage
    # external = browser.find_by_name('sm-from-respondent')

    return len(internals) == 1


def view_full_conversation_date_time_msg_details():
    internals = browser.find_by_name('sm-from-ons')

    # TODO Enable this when we are able to send message from Front-stage
    # externals = browser.find_by_name('sm-from-respondent')

    return len(internals.find_by_name('sm-sent-date'))


def view_last_anchored_message():
    last_message = browser.find_by_name('latest-message')
    return len(last_message.find_by_id('sm-from-ons-1')) == 1
