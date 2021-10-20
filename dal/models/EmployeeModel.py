from ..extensions import db
from .PersonModel import Person

class Employee(db.Model):
    __tablename__ = "employee"
    person_id = db.Column(db.Integer, db.ForeignKey(Person.id), primary_key=True)
    position = db.Column(db.String(32))
    recruit_date = db.Column(db.DateTime(timezone=True))