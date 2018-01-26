from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(Config.FRONTSTAGE_SERVICE + '/sign-in')


def get_email_address_field():
    email_address_field = browser.find_by_id('username')
    username = {
        'username': email_address_field.find_by_id('username').value
    }
    return username


def get_password_field():
    password_field = browser.find_by_id('password')
    password = {
        'password': password_field.find_by_id('password')
    }
    return password


def get_sign_in_button():
    sign_in_button = browser.find_by_id('SIGN_IN_BUTTON')
    sign_in_button.click()
