from urllib.parse import urlencode

from acceptance_tests import browser
from config import Config


def go_to(respondent_details_dict):
    # TODO This must be updated when the method of passing respondent details is finalised

    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}'
                  "/messages/create-message?"
                  f"{urlencode({'ru_details': urlencode(respondent_details_dict)})}")


def found_respondent_details():
    # TODO This must be updated when the method of passing respondent details is finalised

    return {'survey': 'BRES 2017',
            'ru_ref': '49900000498',
            'business': 'Bolts & Rachets Ltd',
            'to': 'Jacky Turner',
            'to_uuid': 'f62dfda8-73b0-4e0e-97cf-1b06327a6712',
            'to_ru_id': 'c614e64e-d981-4eba-b016-d9822f09a4fb'}


def get_ru_details_attributes():
    ru_details_table = browser.find_by_id("create-message-form").first
    ru_details_table_attributes = {'survey': ru_details_table.find_by_id('hidden_survey').value,
                                   'ru_ref': ru_details_table.find_by_id('hidden_ru_ref').value,
                                   'business': ru_details_table.find_by_id('hidden_business').value,
                                   'to': ru_details_table.find_by_id('hidden_to').value,
                                   'to_uuid': ru_details_table.find_by_id('hidden_to_uuid').value,
                                   'to_ru_id': ru_details_table.find_by_id('hidden_to_ru_id').value}
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


def get_first_flashed_message():
    return browser.find_by_id("flashed-message-1").value
