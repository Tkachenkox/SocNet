from ..extensions import db
from .BaseMixin import BaseMixin

class Skill(BaseMixin, db.Model):
    __tablename__ = "skill"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))