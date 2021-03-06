from behave import given, when, then
from acceptance_tests.features.pages import collection_exercise
from common.browser_utilities import wait_for

from logging import getLogger

from structlog import wrap_logger

logger = wrap_logger(getLogger(__name__))


@given('collection exercises for {survey} exist in the system')
def collection_exercises_for_a_survey_exist_in_the_system(_, survey):
    pass


@when('the internal user views the collection exercise page for {survey}')
def internal_user_views_the_collection_exercise_page_for_survey(_, survey):
    collection_exercise.go_to(survey)


@then('the internal user can view relevant attributes for QBS')
def internal_user_can_view_relevant_attributes_for_qbs(context):
    attributes = collection_exercise.get_survey_attributes()
    for row in context.table:
        assert attributes['survey_id'] == row['survey_id']
        assert attributes['survey_title'] == row['survey_title']
        assert attributes['survey_abbreviation'] == row['survey_abbreviation']
        assert attributes['survey_legal_basis'] == row['survey_legal_basis']


@then('the internal user can view all collection exercises for QBS')
def the_internal_user_can_view_all_collection_exercises_for_qbs(context):
    # Validate collection exercise table headers
    table_headers = collection_exercise.get_table_headers()
    required_headers = ['Period', 'Respondent sees', 'Status', 'Sample', 'Report (CSV)', 'MPS', 'Go live', 'Return by']
    assert table_headers == ' '.join(required_headers)

    # Validate rows to ensure values are in the correct columns
    collection_exercises = wait_for(collection_exercise.get_collection_exercises, 16, 2)
    for row in context.table:
        collection_exercises_by_period = next(filter(lambda ce: ce['exercise_ref'] == row['period'],
                                                     collection_exercises))
        assert collection_exercises_by_period['exercise_ref'] == row['period']
        assert collection_exercises_by_period['user_description'] == row['shown_to_respondent_as']


@then('there is at least one collection exercise')
def there_is_at_least_one_collection_exercise(_):
    collection_exercises = wait_for(collection_exercise.get_collection_exercises, 16, 2)
    assert len(collection_exercises) > 0

