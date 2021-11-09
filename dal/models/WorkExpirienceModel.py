from .BaseMixin import BaseMixin
from ..extensions import db


class WorkExperience(BaseMixin, db.Model):
    __tablename__ = 'work_exp'
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    begin_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
