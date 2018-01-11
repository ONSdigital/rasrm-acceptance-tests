from behave import given, when, then


@given('the user is signed into their account')
def signed_in(context):
    context.browser.find_by_id('username').send_keys('rhiannon.griffiths@ons.gov.uk')
    context.browser.find_by_id('password').send_keys('Gizmo007!')
    context.browser.find_by_id('SIGN_IN_BUTTON').click()
