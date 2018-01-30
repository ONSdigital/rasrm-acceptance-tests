import json

import requests

from config import Config


def execute_collection_exercise():
    url = Config.COLLECTION_EXERCISE + '/collectionexercises/survey/c23bb1c1-5202-43bb-8357-7a07c844308f'
    response = requests.get(url=url, auth=Config.BASIC_AUTH)
    collection_exercises = json.loads(response.text)
    for collection_exercise in collection_exercises:
        if collection_exercise['exerciseRef'] == '201801':
            collection_exercise_id = collection_exercise['id']
    requests.post(url=(Config.COLLECTION_EXERCISE + '/collectionexerciseexecute/' + collection_exercise_id),
                  auth=Config.BASIC_AUTH)
