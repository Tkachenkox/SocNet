import json

from dal import Test


class TestSerializer:
    def __init__(self, test: Test):
        questions = json.loads(test.questions)
        questions_returnable = []
        for i in questions:
            questions_returnable.append({f'{k}':i[k] for k in i if k != 'correct_answer'})
        self.data = {
            'id': test.id,
            'skill_id': test.skill_id,
            'creator_id': test.creator_id,
            'name': test.name,
            'questions': questions_returnable,
        }
        self.count = len(questions_returnable)
