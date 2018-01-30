import os


class Config(object):
    PROTOCOL = os.getenv('PROTOCOL', 'http')
    INFO = '/info'

    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')

    ACTION_SERVICE_HOST = os.getenv('ACTION_SERVICE_HOST', 'localhost')
    ACTION_SERVICE_PORT = os.getenv('ACTION_SERVICE_PORT', 8151)
    ACTION_SERVICE = '{}://{}:{}'.format(PROTOCOL, ACTION_SERVICE_HOST, ACTION_SERVICE_PORT)

    ACTION_EXPORTER_HOST = os.getenv('ACTION_EXPORTER_HOST', 'localhost')
    ACTION_EXPORTER_PORT = os.getenv('ACTION_EXPORTER_PORT', 8141)
    ACTION_EXPORTER = '{}://{}:{}'.format(PROTOCOL, ACTION_EXPORTER_HOST, ACTION_EXPORTER_PORT)

    BACKSTAGE_SERVICE_HOST = os.getenv('BACKSTAGE_SERVICE_HOST', 'localhost')
    BACKSTAGE_SERVICE_PORT = os.getenv('BACKSTAGE_SERVICE_PORT', 8001)
    BACKSTAGE_SERVICE = '{}://{}:{}'.format(PROTOCOL, BACKSTAGE_SERVICE_HOST, BACKSTAGE_SERVICE_PORT)

    BACKSTAGE_UI_HOST = os.getenv('BACKSTAGE_UI_HOST', 'localhost')
    BACKSTAGE_UI_PORT = os.getenv('BACKSTAGE_UI_PORT', 8050)
    BACKSTAGE_UI = '{}://{}:{}'.format(PROTOCOL, BACKSTAGE_UI_HOST, BACKSTAGE_UI_PORT)

    CASE_SERVICE_HOST = os.getenv('CASE_SERVICE_HOST', 'localhost')
    CASE_SERVICE_PORT = os.getenv('CASE_SERVICE_PORT', 8171)
    CASE_SERVICE = '{}://{}:{}'.format(PROTOCOL, CASE_SERVICE_HOST, CASE_SERVICE_PORT)

    COLLECTION_EXERCISE_SERVICE_HOST = os.getenv('COLLECTION_EXERCISE_SERVICE_HOST', 'localhost')
    COLLECTION_EXERCISE_SERVICE_PORT = os.getenv('COLLECTION_EXERCISE_SERVICE_PORT', 8145)
    COLLECTION_EXERCISE = '{}://{}:{}'.format(PROTOCOL,
                                              COLLECTION_EXERCISE_SERVICE_HOST,
                                              COLLECTION_EXERCISE_SERVICE_PORT)

    COLLECTION_INSTRUMENT_SERVICE_HOST = os.getenv('COLLECTION_INSTRUMENT_SERVICE_HOST', 'localhost')
    COLLECTION_INSTRUMENT_SERVICE_PORT = os.getenv('COLLECTION_INSTRUMENT_SERVICE_PORT', 8002)
    COLLECTION_INSTRUMENT_SERVICE = '{}://{}:{}'.format(PROTOCOL,
                                                        COLLECTION_INSTRUMENT_SERVICE_HOST,
                                                        COLLECTION_INSTRUMENT_SERVICE_PORT)

    DJANGO_SERVICE_HOST = os.getenv('DJANGO_SERVICE_HOST', 'localhost')
    DJANGO_SERVICE_PORT = os.getenv('DJANGO_SERVICE_PORT', 8040)
    DJANGO_SERVICE = '{}://{}:{}'.format(PROTOCOL, DJANGO_SERVICE_HOST, DJANGO_SERVICE_PORT)

    FRONTSTAGE_API_SERVICE_HOST = os.getenv('FRONTSTAGE_API_SERVICE_HOST', 'localhost')
    FRONTSTAGE_API_SERVICE_PORT = os.getenv('FRONTSTAGE_API_SERVICE_PORT', 8083)
    FRONTSTAGE_API_SERVICE = '{}://{}:{}'.format(PROTOCOL, FRONTSTAGE_API_SERVICE_HOST, FRONTSTAGE_API_SERVICE_PORT)

    FRONTSTAGE_SERVICE_HOST = os.getenv('FRONTSTAGE_SERVICE_HOST', 'localhost')
    FRONTSTAGE_SERVICE_PORT = os.getenv('FRONTSTAGE_SERVICE_PORT', 8082)
    FRONTSTAGE_SERVICE = '{}://{}:{}'.format(PROTOCOL, FRONTSTAGE_SERVICE_HOST, FRONTSTAGE_SERVICE_PORT)

    IAC_SERVICE_HOST = os.getenv('IAC_SERVICE_HOST', 'localhost')
    IAC_SERVICE_PORT = os.getenv('IAC_SERVICE_PORT', 8121)
    IAC_SERVICE = '{}://{}:{}'.format(PROTOCOL, IAC_SERVICE_HOST, IAC_SERVICE_PORT)

    NOTIFY_GATEWAY_SERVICE_HOST = os.getenv('NOTIFY_GATEWAY_SERVICE_HOST', 'localhost')
    NOTIFY_GATEWAY_SERVICE_PORT = os.getenv('NOTIFY_GATEWAY_SERVICE_PORT', 8181)
    NOTIFY_GATEWAY_SERVICE = '{}://{}:{}'.format(PROTOCOL, NOTIFY_GATEWAY_SERVICE_HOST, NOTIFY_GATEWAY_SERVICE_PORT)

    PARTY_SERVICE_HOST = os.getenv('PARTY_SERVICE_HOST', 'localhost')
    PARTY_SERVICE_PORT = os.getenv('PARTY_SERVICE_PORT', 8081)
    PARTY_SERVICE = '{}://{}:{}'.format(PROTOCOL, PARTY_SERVICE_HOST, PARTY_SERVICE_PORT)

    RESPONSE_OPERATIONS_UI_HOST = os.getenv('RESPONSE_OPERATIONS_UI_HOST', 'localhost')
    RESPONSE_OPERATIONS_UI_PORT = os.getenv('RESPONSE_OPERATIONS_UI_PORT', 8085)
    RESPONSE_OPERATIONS_UI = '{}://{}:{}'.format(PROTOCOL, RESPONSE_OPERATIONS_UI_HOST, RESPONSE_OPERATIONS_UI_PORT)

    SAMPLE_SERVICE_HOST = os.getenv('SAMPLE_SERVICE_HOST', 'localhost')
    SAMPLE_SERVICE_PORT = os.getenv('SAMPLE_SERVICE_PORT', 8125)
    SAMPLE_SERVICE = '{}://{}:{}'.format(PROTOCOL, SAMPLE_SERVICE_HOST, SAMPLE_SERVICE_PORT)

    SECURE_MESSAGE_SERVICE_HOST = os.getenv('SECURE_MESSAGE_SERVICE_HOST', 'localhost')
    SECURE_MESSAGE_SERVICE_PORT = os.getenv('SECURE_MESSAGE_SERVICE_PORT', 5050)
    SECURE_MESSAGE_SERVICE = '{}://{}:{}'.format(PROTOCOL, SECURE_MESSAGE_SERVICE_HOST, SECURE_MESSAGE_SERVICE_PORT)

    SURVEY_SERVICE_HOST = os.getenv('SURVEY_SERVICE_HOST', 'localhost')
    SURVEY_SERVICE_PORT = os.getenv('SURVEY_SERVICE_PORT', 8080)
    SURVEY_SERVICE = '{}://{}:{}'.format(PROTOCOL, SURVEY_SERVICE_HOST, SURVEY_SERVICE_PORT)

    CF_DATABASE_TOOL_HOST = os.getenv('CF_DATABASE_TOOL_HOST', 'localhost')
    CF_DATABASE_TOOL_PORT = os.getenv('CF_DATABASE_TOOL_PORT', 9000)
    CF_DATABASE_TOOL = '{}://{}:{}'.format(PROTOCOL, CF_DATABASE_TOOL_HOST, CF_DATABASE_TOOL_PORT)

    SECURITY_USER_NAME = os.getenv('SECURITY_USER_NAME', 'admin')
    SECURITY_USER_PASSWORD = os.getenv('SECURITY_USER_PASSWORD', 'secret')
    BASIC_AUTH = (SECURITY_USER_NAME, SECURITY_USER_PASSWORD)

    PARTY_DATABASE_URI = os.getenv('PARTY_DATABASE_URI', "postgres://postgres:postgres@localhost:6432/postgres")
    DJANGO_OAUTH_DATABASE_URI = os.getenv('DJANGO_OAUTH_DATABASE_URI', "postgres://postgres:postgres@localhost:6432/postgres")
