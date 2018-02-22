import requests

from acceptance_tests import browser
from config import Config
from controllers.case_controller import post_case_event
from controllers.collection_exercise_controller import get_collection_exercise
from controllers.database_controller import get_iac_for_collection_exercise, enrol_party
from controllers.django_oauth_controller import verify_user
from controllers.party_controller import register_respondent


class RespondentDetails:

    def __init__(self):
        self._respondent_id = None
        self._ru_id = None
        self._ru_ref = None

    @staticmethod
    def _create_respondent():
        collection_exercise_id = get_collection_exercise(
            'cb8accda-6118-4d3b-85a3-149e28960c54',
            '201801')['id']
        enrolment_code = get_iac_for_collection_exercise(collection_exercise_id)
        respondent_party = register_respondent(email_address='ropstest@example.com',
                                               first_name='first_name',
                                               last_name='last_name',
                                               password='secret',
                                               phone_number='0187654321',
                                               enrolment_code=enrolment_code)
        verify_user(respondent_party['emailAddress'])
        case_id = enrol_party(respondent_party['id'])
        post_case_event(case_id, respondent_party['id'], "RESPONDENT_ENROLED", "Respondent enrolled")
        return respondent_party['id']

    def _retrieve_respondent_and_ru_details(self):
        if not self._respondent_id:
            self._respondent_id = self._create_respondent()
            url = f'{Config.PARTY_SERVICE}/party-api/v1/respondents/id/{self._respondent_id}'
            response = requests.get(url=url, auth=Config.BASIC_AUTH)
            response.raise_for_status()
            respondent_details = response.json()
            self._ru_id = respondent_details['associations'][0]['partyId']
            self._ru_ref = respondent_details['associations'][0]['sampleUnitRef']

    def get_respondent_id(self):
        if not self._respondent_id:
            self._retrieve_respondent_and_ru_details()
        return self._respondent_id

    def get_ru_id(self):
        if not self._ru_id:
            self._retrieve_respondent_and_ru_details()
        return self._ru_id

    def get_ru_ref(self):
        if not self._ru_ref:
            self._retrieve_respondent_and_ru_details()
        return self._ru_ref


RESPONDENT_DETAILS = RespondentDetails()


def go_to():
    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}'
                  "/reporting-units/"
                  f"{RESPONDENT_DETAILS.get_ru_ref()}")
    browser.find_by_id("create-message-button-1").click()
    assert "messages/create-message" in browser.url


def get_ru_details_attributes():
    ru_details_table = browser.find_by_id("create-message-form").first
    ru_details_table_attributes = {'survey': ru_details_table.find_by_id('hidden_survey').value,
                                   'ru_ref': ru_details_table.find_by_id('hidden_ru_ref').value,
                                   'business': ru_details_table.find_by_id('hidden_business').value,
                                   'to': ru_details_table.find_by_id('hidden_to').value,
                                   'to_uuid': ru_details_table.find_by_id('hidden_to_uuid').value,
                                   'to_ru_id': ru_details_table.find_by_id('hidden_to_ru_id').value}
    return ru_details_table_attributes


def found_respondent_details():
    return {'ru_ref': RESPONDENT_DETAILS.get_ru_ref(),
            'to': 'first_name last_name',
            'to_uuid': RESPONDENT_DETAILS.get_respondent_id(),
            'to_ru_id': RESPONDENT_DETAILS.get_ru_id()}


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
