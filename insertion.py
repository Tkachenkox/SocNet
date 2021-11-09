import datetime
import os
import random
import sys
from uuid import uuid4
import uuid
from flask import url_for
from faker import Faker
import random
from config import Config
from dal.models import Person, Skill, Role
from main import app, db

skills = ['skill1', 'skill2', 'skill3', 'skill4']

def up():
    fake_data = Faker()
    with app.app_context():
        for i in skills:
            skill = Skill(
                name = i
            )
            db.session.add(skill)

        role1 = Role(
            name = 'user',
            is_admin = False,
            is_superuser = False,
        )
        db.session.add(role1)
        
        role2 = Role(
            name = 'admin',
            is_admin = True,
            is_superuser = False,
        )
        db.session.add(role2)
        
        role3 = Role(
            name = 'super_user',
            is_admin = True,
            is_superuser = True,
        )
        db.session.add(role3)
        
        db.session.commit()

        for i in range(10):
            person = Person(first_name=fake_data.first_name(),
                            second_name=fake_data.last_name(),
                            last_name=fake_data.suffix(),
                            create_date=fake_data.date_between_dates(date_start=datetime.date(
                                2016, 12, 7), date_end=datetime.date(2020, 1, 17)),
                            birthday=fake_data.date_of_birth(
                                minimum_age=18, maximum_age=50),
                            phone_number=fake_data.msisdn(),
                            email=(fake_data.ascii_email()),
                            position = fake_data.job()[:32],
                            role_id = random.randint(0, 2) + 1
                            )
            person.set_password("password")
            db.session.add(person)

        db.session.commit()


def delete():
    with app.app_context():
        db.session.query(Person).delete()
        db.session.commit()


if __name__ == '__main__':
    try:
        if sys.argv[1] == 'up':
            up()
        elif sys.argv[1] == 'down':
            delete()
        else:
            print(f'Incorrect arg {sys.argv[1]}')
    except Exception as e:
        print(f'Error: {e}')
