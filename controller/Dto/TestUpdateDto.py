class TestUpdateDto:

    def __init__(self, data: dict):
        self.data = {
            'skill_id': data.get('skill_id'),
            'name': data.get('name'),
            'questions': data.get('questions')
        }