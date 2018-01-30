import logging

import requests
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def register_respondent(email_address, first_name, last_name, password, phone_number, enrolment_code):
    logger.debug('Post respondent to party service')

    registration_data = {
        'emailAddress': email_address,
        'firstName': first_name,
        'lastName': last_name,
        'password': password,
        'telephone': phone_number,
        'enrolmentCode': enrolment_code
    }

    url = Config.PARTY_SERVICE + '/party-api/v1/respondents'

    response = requests.post(url, json=registration_data, auth=Config.BASIC_AUTH)

    return response.text
