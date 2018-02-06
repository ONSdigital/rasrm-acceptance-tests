from urllib.parse import urlencode

from acceptance_tests import browser
from config import Config


def go_to(respondent_details_dict):
    # TODO This must be updated when the method of passing respondent details is finalised

    browser.visit('{}/messages/create-message?ru={}'
                  .format(Config.RESPONSE_OPERATIONS_UI, urlencode(respondent_details_dict)))


def found_respondent_details():
    # TODO This must be updated when the method of passing respondent details is finalised

    return {'survey': 'BRES 2017',
            'ru_ref': '36509908341B',
            'business': 'Bolts & Rachets Ltd',
            'to': 'Jacky Turner'}


def click_message_send_button():
    browser.find_by_id('send-message').click()


def click_cancel_button():
    browser.find_by_id('cancel-button').click()


def enter_text_in_message_subject(text):
    browser.driver.find_element_by_id('secure-message-subject').send_keys(text)


def enter_text_in_message_body(text):
    browser.driver.find_element_by_id('secure-message-body').send_keys(text)


def message_subject_text():
    return browser.driver.find_element_by_id('secure-message-subject').text


def message_body_text():
    return browser.driver.find_element_by_id('secure-message-body').text
