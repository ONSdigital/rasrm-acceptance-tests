import time
from logging import getLogger

from itsdangerous import TimestampSigner, URLSafeTimedSerializer
from structlog import wrap_logger

from config import Config

logger = wrap_logger(getLogger(__name__))


def generate_email_token(email):
    secret_key = Config.SECRET_KEY
    email_token_salt = Config.EMAIL_TOKEN_SALT

    if secret_key is None or email_token_salt is None:
        msg = "SECRET_KEY or EMAIL_TOKEN_SALT are not configured."
        logger.error(msg)

    timed_serializer = URLSafeTimedSerializer(secret_key)
    return timed_serializer.dumps(email, salt=email_token_salt)


class ExpiredTimestampSigner(TimestampSigner):
    def get_timestamp(self):
        # Make the signature timestamp a year old
        return int(time.time()) - 60 * 60 * 24 * 365


def generate_expired_email_token(email):
    secret_key = Config.SECRET_KEY
    email_token_salt = Config.EMAIL_TOKEN_SALT

    if secret_key is None or email_token_salt is None:
        msg = "SECRET_KEY or EMAIL_TOKEN_SALT are not configured."
        logger.error(msg)
    timed_serializer = URLSafeTimedSerializer(secret_key, signer=ExpiredTimestampSigner)
    return timed_serializer.dumps(email, salt=email_token_salt)
