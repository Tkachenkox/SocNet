from ..extensions import db
from .PersonModel import Person
from .SkillModel import Skill
from .BaseMixin import BaseMixin

class Test(BaseMixin, db.Model):
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey(Skill.id), index=True, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey(Person.id), index=True, nullable=False)
    max_point = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    questions = db.Column(db.String(), nullable=False)