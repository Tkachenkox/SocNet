from ..extensions import db
from datetime import datetime
from .PersonModel import Person
from .TestModel import Test
from .BaseMixin import BaseMixin

class TestResult(BaseMixin, db.Model):
    __tablename__ = "test_result"
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey(Test.id), index=True, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey(Person.id), index=True, nullable=False)
    begin_date = db.Column(db.DateTime(timezone=True),  default=datetime.utcnow, nullable=False)
    end_date = db.Column(db.DateTime(timezone=True))
    count_questions = db.Column(db.Integer)
    correct_answers = db.Column(db.Integer)
    additional_skill_point = db.Column(db.Integer)