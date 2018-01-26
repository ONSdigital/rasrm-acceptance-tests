from behave import given, when, then


@given('the user has selected to add a new survey')
@given('selects to add a new survey')
@when('they add a new survey')
def add_a_new_survey(context):
    context.find_by_id('ADD_SURVEY_BTN').click()


@then('they are able to enter the enrolment code')
def enter_enrolment_code(context):
    context.find_by_id('ENROLMENT_CODE_FIELD')


@given('the user has entered a valid enrolment code')
@given('the user has entered their enrolment code')
@when('they enter a valid enrolment code')
def enter_valid_enrolment_code(context):
    context.browser.find_by_id('ENROLMENT_CODE_FIELD').send_keys()
    context.browser.find_by_id('CONTINUE_BTN').click()


@then('they are to be presented with the survey and organisation that they are enrolling for')
def view_confirmation_page(context):
    context.browser.find_by_id('')


@when('they enter an invalid enrolment code')
def enter_invalid_enrolment_code(context):
    context.browser.find_by_id('ENROLMENT_CODE_FIELD').send_keys('222thu78nj7m')
    context.browser.find_by_id('CONTINUE_BTN').click()


@then('they are to be notified')
def invalid_enrolment_code_notification(context):
    context.find_by_id('')


@when('they continue and confirm that the organisation and survey that they are enrolling for is correct')
def confirm_organisation_and_continue(context):
    context.browser.find_by_id('CONTINUE_BTN').click()


@then('the new survey is to be listed in My Surveys')
def new_survey_listed(context):
    context.find_by_id('')


@then('confirmation is presented to the user')
def confirmation_presented_for_new_survey(context):
    context.browser.find_by_id('NEW_SURVEY_NOTIF')


@when('they navigate to the confirm organisation page and click cancel')
def click_cancel(context):
    context.browser.find_by_id().click('CANCEL_BTN')


@then('the user is navigated back to their "To do" list and have not enrolled for that survey')
def view_todo_list(context):
    context.find_by_id('')
