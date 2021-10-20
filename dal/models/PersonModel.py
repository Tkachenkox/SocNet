from ..extensions import db
from .DateMixin import DateMixin

class Person(DateMixin, db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    second_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100))
    birthday = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(15), unique=True, index=True)
    email = db.Column(db.String(32), unique=True, index=True)
    password = db.Column(db.String(256))
