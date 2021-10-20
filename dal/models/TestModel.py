from ..extensions import db
from .EmployeeModel import Employee
from .SkillModel import Skill

class Test(db.Model):
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey(Skill.id), index=True)
    creator_id = db.Column(db.Integer, db.ForeignKey(Employee.person_id), index=True)
    name = db.Column(db.String(32))
    questions = db.Column(db.String())