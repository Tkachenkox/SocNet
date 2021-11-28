from dal.models import Test
import json

class TestCreateDto:

    def __init__(self, test: dict, user_id: int):
        self.data = {
            'skill_id': test.get('skill_id'),
            'max_point': test.get('max_point'),
            'creator_id': user_id,
            'name': test.get('name'),
            'questions': json.dumps(test.get('questions')),
        }