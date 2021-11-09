from dateutil.parser import parse
from wtforms import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired, Email, Optional

from .BaseValidation import check_email, is_phone_valid, is_valid_date


class PersonValidator(Form):
    first_name = StringField(
        'first_name', [DataRequired(message='Empty field')])
    second_name = StringField(
        'second_name', [DataRequired(message='Empty field')])
    last_name = StringField('last_name', [Optional()])
    birthday = StringField(
        'birthday', [DataRequired(message='Empty field'), is_valid_date])
    phone_number = StringField(
        'phone_number', [DataRequired(message='Empty field'), is_phone_valid])
    email = StringField('email', [DataRequired(
        message='Empty field'), Email(message='Incorrect email')])


class PersonUpdateValidator(Form):
    first_name = StringField('first_name', [Optional()])
    second_name = StringField('second_name', [Optional()])
    last_name = StringField('last_name', [Optional()])
    birthday = StringField('birthday', [is_valid_date])
    phone_number = StringField('phone_number', [is_phone_valid])
    email = StringField('email', [check_email])
