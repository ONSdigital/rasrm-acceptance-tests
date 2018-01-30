from acceptance_tests import browser

from controllers import collection_exercise_controller, database_controller, sample_controller


def after_all(context):
    """
    Close the browser after testing. See https://pythonhosted.org/behave/tutorial.html#environmental-controls
    """
    browser.quit()


def before_all(context):
        database_controller.reset_database('resources/database/databasereset.sql')


def enrolment_setup():
    test_file = 'resources/sample_files/us334-add_a_survey/sample_file_existing_survey.csv'
    sample_controller.load_sample(test_file=test_file)
    collection_exercise_controller.execute_collection_exercise()
    valid_enrolment_code = database_controller.select_iac()
