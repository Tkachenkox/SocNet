from dal.models import Test
import json

class TestCreateDto:

    def __init__(self, test: dict):
        self.data = {
            'skill_id': test.get('skill_id'),
            'creator_id': test.get('creator_id'),
            'name': test.get('name'),
            'questions': json.dumps(test.get('questions')),
        }