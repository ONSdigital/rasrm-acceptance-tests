from behave import given, when, then


@given('the user has selected to add a new survey')
@given('selects to add a new survey')
@when('they add a new survey')
def add_a_new_survey(context):
    context.find_by_id('ADD_SURVEY_BTN').click


@then('they are able to enter the enrolment code')
def enter_enrolment_code(context):
    context.find_by_id('ENROLMENT_CODE_FIELD')


@when('they enter a valid enrolment code')
def enter_valid_enrolment_code(context):
    context.find_by_id('ENROLMENT_CODE_FIELD').send_keys('')


@then('they are to be presented with the survey and organisation that they are enrolling for')
def view_confirmation_page(context):
    context.find_by_id('')


@when('they enter an invalid enrolment code')
def enter_invalid_enrolment_code(context):
    context.find_by_id('ENROLMENT_CODE_FIELD').send_keys('222thu78nj7m')
    context.find_by_id('')
