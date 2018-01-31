from acceptance_tests import browser

from controllers import collection_exercise_controller, database_controller, sample_controller, party_controller, django_oauth_controller, case_controller
from config import Config
from acceptance_tests.features.steps import common


def after_all(context):
    """
    Close the browser after testing. See https://pythonhosted.org/behave/tutorial.html#environmental-controls
    """
    browser.quit()


def before_all(context):
    database_controller.reset_rm_database('resources/database/database_reset_rm.sql')
    database_controller.reset_ras_database()
    common.signed_in_frontstage(context)
    enrolment_setup()


def enrolment_setup():
    test_file = 'resources/sample_files/business-survey-sample-date.csv'
    sample_controller.load_sample(test_file=test_file)
    collection_exercise_controller.execute_collection_exercise()
    valid_enrolment_code = database_controller.select_iac()
    respondent_info = party_controller.register_respondent(email_address=Config.RESPONDENT_USERNAME,
                                                           first_name='first_name',
                                                           last_name='last_name',
                                                           password=Config.RESPONDENT_PASSWORD,
                                                           phone_number='0987654321',
                                                           enrolment_code=valid_enrolment_code
                                                           )

    respondent_uuid = respondent_info['id']

    django_oauth_controller.verify_user(respondent_info['emailAddress'])

    case_id = database_controller.enrol_party(respondent_uuid)

    case_controller.post_case_event(case_id, respondent_uuid, "RESPONDENT_ENROLED", "Respondent enrolled")
