import json
from datetime import datetime

from app.exceptions import TestException
from app.validation import TestValidator
from dal import Test, db

from .dto import TestSerializer, TestSerializerView


class TestService:

    def add(self, data: dict) -> int:
        try:
            form = TestValidator(data=data)
            if form.validate():
                new_test = Test(
                    skill_id = data.get('skill_id'),
                    creator_id = data.get('creator_id'),
                    name = data.get('name'),
                    questions = data.get('questions'),
                )
                db.session.add(new_test)
                db.session.commit()
                return new_test.id
            else:
                return form.errors
        except Exception as e:
            raise TestException(e)
        
    def get_by_id(self, id: int) -> dict:
        try:
            test = Test.query.filter_by(id=id, remove_date=None).first()
            if test:
                return TestSerializerView(test).data
            return None
        except Exception as e:
            raise TestException(e)

    def get_all(self, page: int, on_page: int, sort_by: str) -> list:
        try:
            tests_return = []
            if sort_by == 'name':
                sort_row = Test.name
            elif sort_by == 'creator':
                sort_row = Test.creator_id
            elif sort_by == 'skill':
                sort_row = Test.skill_id
            else:
                sort_row = Test.create_date
            tests_from_db = db.session.query(
                Test.id,
                Test.skill_id,
                Test.creator_id,
                Test.name
            ).order_by(sort_row.asc()).\
                filter(Test.remove_date.is_(None)).paginate(page, on_page, False)
            tests_return = [self.__make_dict_without_questions(i) for i in tests_from_db.items]
            return tests_return
        except Exception as e:
            raise TestException(e)


    def update(self, id: int, data: dict) -> bool:
        pass

    def delete(self, id: int) -> bool:
        pass

    def start_test(self, id: int) -> dict:
        try:
            test = Test.query.filter_by(id=id, remove_date=None).first()
            if test:
                return TestSerializer(test).data
            return None
        except Exception as e:
            raise TestException(e)


    def check_result(self, id: int, data: dict):
        pass

    def __make_dict_without_questions(self, row: set) -> dict:
        return {
            'id': row[0],
            'skill': row[1],
            'creator': row[2],
            'name': row[3]
        }
