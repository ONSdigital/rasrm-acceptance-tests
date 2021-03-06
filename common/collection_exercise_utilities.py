import time
from datetime import datetime, timedelta
from logging import getLogger

from dateutil import tz
from dateutil.tz import tzlocal
from structlog import wrap_logger

import common.string_utilities
from controllers import case_controller, collection_exercise_controller, database_controller, party_controller, \
    sample_controller
from controllers.collection_exercise_controller import post_event_to_collection_exercise, convert_datetime_for_event
from controllers.collection_instrument_controller import get_collection_instruments_by_classifier, \
    link_collection_instrument_to_exercise, upload_seft_collection_instrument
from controllers.database_controller import poll_collection_exercise_until_state_changed

logger = wrap_logger(getLogger(__name__))

FIELD_SEPARATOR = '-'
USER_DESCRIPTION_SOCIAL_PREFIX = 'SOCIAL'
USER_DESCRIPTION_BUSINESS_PREFIX = 'BUSINESS'


def execute_collection_exercises():
    logger.info('Executing collection exercises')
    # Bricks
    execute_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54', '201801')
    execute_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54', '201812')
    # QBS
    execute_collection_exercise('02b9c366-7397-42f7-942a-76dc5876d86d', '1806', ci_type='eQ')
    execute_collection_exercise('02b9c366-7397-42f7-942a-76dc5876d86d', '1809', ci_type='eQ')

    logger.info('Waiting for collection exercises to finish executing')
    poll_database_for_iac(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801')
    poll_database_for_iac(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201812')
    poll_database_for_iac(survey_id='02b9c366-7397-42f7-942a-76dc5876d86d', period='1806')
    poll_database_for_iac(survey_id='02b9c366-7397-42f7-942a-76dc5876d86d', period='1809')
    logger.info('Collection exercises have finished executing')


def execute_collection_exercise(survey_id, period, ci_type='SEFT', performance_test=False):
    logger.info('Executing collection exercise', survey_id=survey_id, period=period, ci_type=ci_type)
    collection_exercise = collection_exercise_controller.get_collection_exercise(survey_id, period)

    if ci_type == 'eQ':
        collection_instruments = get_collection_instruments_by_classifier(survey_id, form_type='0001')
        for collection_instrument in collection_instruments:
            link_collection_instrument_to_exercise(collection_instrument['id'], collection_exercise['id'])
    else:
        upload_seft_collection_instrument(collection_exercise['id'],
                                          'resources/collection_instrument_files/064_201803_0001.xlsx',
                                          form_type='0001')

    sample_filename = 'performance-test-sample.csv' if performance_test else 'resources/sample_files/business-survey-sample-date.csv'
    sample_summary = sample_controller.upload_sample(collection_exercise['id'], sample_filename)
    collection_exercise_controller.link_sample_summary_to_collection_exercise(collection_exercise['id'],
                                                                              sample_summary['id'])
    poll_collection_exercise_until_state_changed(collection_exercise['id'], 'READY_FOR_REVIEW')
    collection_exercise_controller.execute_collection_exercise(survey_id, period)
    logger.info('Successfully executed collection exercise', survey_id=survey_id, period=period, ci_type=ci_type)


def poll_database_for_iac(survey_id, period, social=False, count=1):
    logger.info('Waiting for collection exercise execution process to finish',
                survey_id=survey_id, period=period)
    collection_exercise_id = collection_exercise_controller.get_collection_exercise(survey_id, period)['id']
    attempt = 1
    while attempt <= 20:
        logger.info("Getting iac code for collection exercise",
                    collection_exercise_id=collection_exercise_id,
                    social=social,
                    attempt=attempt)
        iac_code = database_controller.get_iac_for_collection_exercise(collection_exercise_id, social=social, count=count)
        if iac_code:
            logger.info('Collection exercise finished executing', survey_id=survey_id, period=period)
            return iac_code
        time.sleep(3)
        attempt += 1
    raise Exception("Failed to get iac code for collection exercise")


def generate_new_enrolment_code(case_id, business_id):
    iac = case_controller.generate_new_enrolment_code(case_id, business_id)
    return iac


def generate_new_enrolment_code_from_existing_code(existing_code):
    case = find_case_by_enrolment_code(existing_code)
    return generate_new_enrolment_code(case['id'], case['partyId'])


def generate_social_collection_exercise_dates():
    """Generates and returns collection exercise dates."""

    now = datetime.utcnow()

    dates = {
        'mps': now + timedelta(seconds=5),
        'go_live': now + timedelta(minutes=5),
        'return_by': now + timedelta(days=10),
        'exercise_end': now + timedelta(days=11)
    }

    return dates


def generate_collection_exercise_dates_from_period(period):
    """Generates a collection exercise events base date from the period supplied."""

    now = datetime.now()
    now = now.replace(tzinfo=tzlocal()).astimezone(tz.gettz('UTC'))
    period_year = int(period[:4])
    period_month = int(period[-2:])

    base_date = datetime(period_year, period_month, now.day, now.hour, now.minute, now.second, now.microsecond)

    return generate_collection_exercise_dates(base_date)


def create_variable_collection_exercise_dates(collection_exercise_id, dates):
    post_event_to_collection_exercise(collection_exercise_id, 'employment',
                                      convert_datetime_for_event(dates['employment']))
    post_event_to_collection_exercise(collection_exercise_id, 'reminder',
                                      convert_datetime_for_event(dates['first_reminder']))
    post_event_to_collection_exercise(collection_exercise_id, 'reminder2',
                                      convert_datetime_for_event(dates['second_reminder']))
    post_event_to_collection_exercise(collection_exercise_id, 'reminder3',
                                      convert_datetime_for_event(dates['third_reminder']))


def generate_collection_exercise_dates(base_date):
    """Generates and returns collection exercise event dates based on the base date supplied."""

    dates = {
        'mps': base_date + timedelta(seconds=5),
        'go_live': base_date + timedelta(minutes=1),
        'return_by': base_date + timedelta(days=10),
        'exercise_end': base_date + timedelta(days=11),
        'employment': base_date + timedelta(days=-30),
        'first_reminder': base_date + timedelta(days=5),
        'second_reminder': base_date + timedelta(days=6),
        'third_reminder': base_date + timedelta(days=7)
    }

    return dates


def make_user_description(user_description_in, is_social_survey, max_field_length):
    if is_social_survey:
        prefix = ''.join((USER_DESCRIPTION_SOCIAL_PREFIX, FIELD_SEPARATOR))
    else:
        prefix = ''.join((USER_DESCRIPTION_BUSINESS_PREFIX, FIELD_SEPARATOR))

    compacted_user_description = common.string_utilities.compact_string(user_description_in,
                                                                        max_field_length - len(prefix))

    return ''.join((prefix, compacted_user_description))


def enrol_respondent(party_id, survey_id, period):
    collection_exercise_id = collection_exercise_controller.get_collection_exercise(survey_id, period)['id']
    enrolment_code = database_controller.get_iac_for_collection_exercise(collection_exercise_id)
    party_controller.add_survey(party_id, enrolment_code)


def find_case_by_enrolment_code(enrolment_code):
    return case_controller.find_case_by_iac(enrolment_code)


def get_party_from_email(email):
    return party_controller.get_party_by_email(email)


def create_business_survey_period(period_offset_days=0):
    period_date = datetime.utcnow() + timedelta(days=period_offset_days)

    return format_period(period_date.year, period_date.month)


def create_social_survey_period(period_offset_days=0):
    period_date = datetime.utcnow() + timedelta(days=period_offset_days)

    return format_period(period_date.year, period_date.month)


def format_period(period_year, period_month):
    return f'{period_year}{str(period_month).zfill(2)}'
