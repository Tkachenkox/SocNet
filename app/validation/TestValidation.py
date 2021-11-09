from wtforms import Form
from wtforms.fields import StringField
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
