from urllib.parse import urlencode

from acceptance_tests import browser
from config import Config


def go_to(respondent_details_dict):
    # TODO This must be updated when the method of passing respondent details is finalised

    browser.visit('{}/messages/create-message?{}'
                  .format(Config.RESPONSE_OPERATIONS_UI, urlencode({'ru': urlencode(respondent_details_dict)})))


def found_respondent_details():
    # TODO This must be updated when the method of passing respondent details is finalised

    return {'survey': 'BRES 2017',
            'ru_ref': '36509908341B',
            'business': 'Bolts & Rachets Ltd',
            'to': 'Jacky Turner'}


def get_ru_details_attributes():
    ru_details_table = browser.find_by_id("ru-details-table").first
    ru_details_table_attributes = {'survey': ru_details_table.find_by_id('survey-label').value,
                                   'ru_ref': ru_details_table.find_by_id('ru-ref-label').value,
                                   'business': ru_details_table.find_by_id('business-label').value,
                                   'to': ru_details_table.find_by_id('to-label').value}
    return ru_details_table_attributes


def get_subject_and_body():
    form_text_fields = browser.find_by_id("create-message-form").first
    form_text_field_attributes = {'subject': form_text_fields.find_by_id('secure-message-subject').value,
                                  'body': form_text_fields.find_by_id('secure-message-body').value}
    return form_text_field_attributes


def click_message_send_button():
    browser.find_by_id('btn-send-message').click()


def click_cancel_button():
    browser.find_by_id('btn-cancel').click()


def enter_text_in_message_subject(text):
    browser.driver.find_element_by_id('secure-message-subject').send_keys(text)


def enter_text_in_message_body(text):
    browser.driver.find_element_by_id('secure-message-body').send_keys(text)


def get_message_subject_text():
    return get_subject_and_body().get('subject')


def get_message_body_text():
    return get_subject_and_body().get('body')


def clear_message_subject_text():
    browser.driver.find_element_by_id('secure-message-subject').clear()


def clear_message_body_text():
    browser.driver.find_element_by_id('secure-message-body').clear()
