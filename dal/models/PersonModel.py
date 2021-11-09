from werkzeug.security import generate_password_hash, check_password_hash

from ..extensions import db
from .BaseMixin import BaseMixin
from .RoleModel import Role

person_skills = db.Table('person_skills',
                            db.Column('person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True),
                            db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True))
                            
class Person(BaseMixin, db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    second_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100))
    birthday = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(15), unique=True, index=True)
    email = db.Column(db.String(32), unique=True, index=True)
    position = db.Column(db.String(32), nullable=False)
    recruit_date = db.Column(db.DateTime(timezone=True))
    level = db.Column(db.Integer, default=1)
    skill_point = db.Column(db.Integer, default=0)
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))
    skills = db.relationship('Skill', secondary=person_skills, lazy='dynamic', backref=db.backref('persons', lazy=True))
    password = db.Column(db.String(256))

    def set_password(self, password):
        self.password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)

