import logging

import requests
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def verify_user(email_address):
    payload = {
        'client_id': Config.SECURITY_USER_NAME,
        'client_secret': Config.SECURITY_USER_PASSWORD,
        'username': email_address,
        'account_verified': 'true'
    }

    url = Config.DJANGO_SERVICE + '/api/account/create'

    response = requests.put(url, auth=Config.BASIC_AUTH, data=payload)

    if response.status_code != 201:
        logger.error("Unable to set the user active on the OAuth2 server")
