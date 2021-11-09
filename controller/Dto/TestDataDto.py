class TestDataDto:

    def __init__(self, skill_id: int, creator_id: int, name: str, questions: dict):
        self.data = {
            'skill_id': skill_id,
            'creator_id': creator_id,
            'name': name,
            'questions': questions
        }