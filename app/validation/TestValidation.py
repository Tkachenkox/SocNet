from wtforms import Form
from wtforms.fields import StringField, IntegerField
from wtforms.validators import DataRequired, Email, Optional

from .BaseValidation import is_valid_questions


class TestValidator(Form):
    skill_id = StringField(
        'skill_id', [DataRequired(message='Empty field')])
    creator_id = StringField(
        'creator_id', [DataRequired(message='Empty field')])
    name = StringField('name', [DataRequired(message='Empty field')])
    questions = StringField(
        'questions', [DataRequired(message='Empty field'), is_valid_questions])
    max_point = IntegerField('max_point', [DataRequired(message='Empty filed')])

class TestUpdateValidator(Form):
    skill_id = StringField('skill_id', [Optional()])
    creator_id = StringField('creator_id', [Optional()])
    name = StringField('name', [Optional()])
    questions = StringField('questions', [Optional(), is_valid_questions])