import logging

from structlog import wrap_logger

from config import Config
from common.request_handler import request_handler


logger = wrap_logger(logging.getLogger(__name__))


def reset_database(sql_script_file_path):
    logger.debug('Executing SQL script', sql_script_file_path)
    url = Config.CF_DATABASE_TOOL + '/sql'
    with open(sql_script_file_path, 'r') as sqlScriptFile:
        sqlScript=sqlScriptFile.read().replace('\n', '')
    response = request_handler('POST', url, auth=Config.BASIC_AUTH, Data=sqlScript)

    if response.status_code != 201:
        logger.error('Database reset failed')

    logger.debug('Database is successfully reset')
    return response.text
