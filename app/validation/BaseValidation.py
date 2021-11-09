import json
import re

from dateutil.parser import parse
from wtforms import Form
from wtforms.fields import StringField
from wtforms.validators import ValidationError


def is_valid_questions(form: Form, field: StringField) -> bool:
    try:
        questions = json.loads(field.data)
        if questions:
            for i in questions:
                print(i)
                question = i.get('question')
                correct_answer = i.get('correct_answer')
                if (question is None or correct_answer is None):
                    raise ValidationError(f'Not valid questions')
            return True
        raise ValidationError(f"Questions can't be null")
    except:
        raise ValidationError(f'Not valid questions')


def parse_date(form: Form, str_date: str) -> bool:
    try:
        if parse(str_date):
            return True
    except:
        raise ValidationError(f'Not correct date')


def is_phone_valid(form: Form, field: StringField):
    if field.data:
        for sym in range(len(field.data)):
            if sym == 0 and field.data[sym] == '+':
                continue
            elif sym > 0 and not field.data[sym].isdigit():
                raise ValidationError(
                    f'Phone number must contains only digits')


def is_valid_date(form: Form, field: StringField):
    if field.data:
        if not parse_date(field.data):
            raise ValidationError(f'{field.name} must be date')


def check_email(form: Form, field: StringField):
    if field.data:
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if not (re.search(regex, field.data)):
            raise ValidationError(f'Incorrect email')
