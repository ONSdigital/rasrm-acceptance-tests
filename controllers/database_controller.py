import logging

import requests
from sqlalchemy import create_engine
from structlog import wrap_logger

from config import Config


logger = wrap_logger(logging.getLogger(__name__))


def reset_rm_database(sql_script_file_path):
    logger.debug('Executing SQL script', sql_script=sql_script_file_path)

    url = Config.CF_DATABASE_TOOL + '/sql'
    headers = {
        'Content-Type': 'text/plain'
    }
    with open(sql_script_file_path, 'r') as sqlScriptFile:
        sql_script = sqlScriptFile.read().replace('\n', '')

    response = requests.post(url, auth=Config.BASIC_AUTH, headers=headers, data=sql_script)

    if response.status_code != 201:
        logger.error('Database reset failed', status=response.status_code)

    logger.debug('Database is successfully reset')
    return response.text


def reset_ras_database():
    engine = create_engine(Config.PARTY_DATABASE_URI)
    connection = engine.connect()
    trans = connection.begin()

    with open('resources/database/database_reset_party.sql', 'r') as sqlScriptFile:
        reset_party_sql = sqlScriptFile.read().replace('\n', '')

    connection.execute(reset_party_sql)
    trans.commit()

    engine = create_engine(Config.DJANGO_OAUTH_DATABASE_URI)
    connection = engine.connect()
    trans = connection.begin()

    with open('resources/database/database_reset_oauth.sql', 'r') as sqlScriptFile:
        reset_oauth_sql = sqlScriptFile.read().replace('\n', '')

    connection.execute(reset_oauth_sql)
    trans.commit()


def select_iac():
    url = Config.CF_DATABASE_TOOL + '/sql'
    headers = {
        'Content-Type': 'text/plain'
    }
    sql_statement = "SELECT c.iac FROM casesvc.case c " \
                    "INNER JOIN iac.iac i ON c.iac = i.code " \
                    "WHERE i.active = true AND i.lastuseddatetime IS NULL AND c.SampleUnitType = 'B' " \
                    "ORDER BY i.createddatetime DESC LIMIT 1;"
    response = requests.post(url, auth=Config.BASIC_AUTH, headers=headers, data=sql_statement)
    return response.text[4:-1]


def enrol_party(respondant_uuid):
    case_id = None

    sql_statement_update_enrolment = f"UPDATE partysvc.enrolment SET status = 'ENABLED' " \
                                     f"WHERE respondent_id = (SELECT id FROM partysvc.respondent " \
                                     f"WHERE party_uuid = '{respondant_uuid}');"
    sql_get_case_id = f"SELECT case_id FROM partysvc.pending_enrolment " \
                      f"WHERE respondent_id = (SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondant_uuid}');"
    sql_delete_pending_enrolment = f"DELETE FROM partysvc.pending_enrolment " \
                                   f"WHERE respondent_id = " \
                                   f"(SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondant_uuid}');"

    engine = create_engine(Config.PARTY_DATABASE_URI)
    connection = engine.connect()

    result = connection.execute(sql_get_case_id)
    for row in result:
        case_id = row['case_id']

    trans = connection.begin()
    connection.execute(sql_statement_update_enrolment)
    connection.execute(sql_delete_pending_enrolment)
    trans.commit()

    return case_id
