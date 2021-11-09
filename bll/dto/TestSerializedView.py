import json

from dal import Test


class TestSerializerView:
    def __init__(self, test: Test):
        self.data = {
            'id': test.id,
            'skill_id': test.skill_id,
            'creator_id': test.creator_id,
            'name': test.name
        }
