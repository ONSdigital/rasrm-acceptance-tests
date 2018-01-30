import requests

from config import Config


def execute_collection_exercise():
    url = Config.COLLECTION_EXERCISE + '/collectionexercises/survey/c23bb1c1-5202-43bb-8357-7a07c844308f'
    collection_exercises = requests.get(url=url, auth=Config.BASIC_AUTH)
    for collection_exercise in collection_exercises:
        if collection_exercise['name'] == '1806':
            collection_exercise_id = collection_exercise['id']
    requests.post(url=(Config.COLLECTION_EXERCISE + '/collectionexerciseexecute/' + collection_exercise_id),
                  auth=Config.BASIC_AUTH)
