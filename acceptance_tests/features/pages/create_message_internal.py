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