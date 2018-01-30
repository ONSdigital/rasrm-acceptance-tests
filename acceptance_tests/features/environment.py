from acceptance_tests import browser
from controllers import database_controller


def after_all(context):
    """
    Close the browser after testing. See https://pythonhosted.org/behave/tutorial.html#environmental-controls
    """
    browser.quit()


def before_all(context):
        database_controller.reset_rm_database('/ras-integration-tests/resources/database/database_reset_rm.sql')
