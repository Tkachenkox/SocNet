from datetime import datetime
from re import T

from sqlalchemy.orm import relation

from app.exceptions import PersonException
from app.validation import PersonUpdateValidator, PersonValidator
from config import Config
from dal import Person, db, person_skills

from bll.SkillService import SkillService

from .dto import PersonSerialized
from .TokenHelper import generate_token


class PersonService:

    def auth(self, data: dict) -> bool:
        email = data["email"]
        password = data["password"]
        person = Person.query.filter_by(email=email).first()
        if person and person.check_password(password):
            return generate_token(person)
        
        return False


    def create(self, data: dict) -> bool:
        form = PersonValidator(data=data)
        if form.validate():
            new_person = Person(
                first_name = data['first_name'],
                second_name = data['second_name'],
                last_name = data['last_name'],
                birthday = data['birthday'],
                phone_number = data['phone_number'],
                email = data['email']
            )
            new_person.set_password(data["password"])

            try:
                db.session.add(new_person)

                db.session.commit()
                
                return new_person.id
            except Exception as e:
                if e.args[0].split('"')[1] == 'ix_person_phone_number':
                    raise PersonException(f"Person with phone number {data['phone_number']} alredy registred")
                else:
                    raise PersonException(f"Person with phone number {data['email']} alredy registred")
        return form.errors

    def get_by_id(self, id: int) -> dict:
        person = Person.query.filter_by(id=id, remove_date=None).first()
        if person:
            return PersonSerialized(person).data
        return None

    def update(id: int, data: dict) -> bool:
        form = PersonUpdateValidator(data=data)
        if form.validate():
            data_update = {i: data[i] for i in data if data[i]}
            try:
                Person.query.filter_by(id=id, remove_date=None).update(data_update)
                db.session.commit()
                return id
            except Exception as e:
                if e.args[0].split('"')[1] == 'ix_person_phone_number':
                    raise PersonException(f"Person with phone number {data['phone_number']} alredy registred")
                else:
                    raise PersonException(f"Person with phone number {data['email']} alredy registred")
        return form.errors


    def get_all(self, sort_field: str, page: int, on_page: int) -> list:
        persons_return = []
        if sort_field == 'name':
            sort_row = Person.first_name
        elif sort_field == 'phone_number':
            sort_row = Person.phone_number
        elif sort_field == 'email':
            sort_row = Person.email
        else:
            sort_row = Person.create_date
        persons_from_db = db.session.query(
            Person.id,
            Person.first_name,
            Person.second_name,
            Person.phone_number,
            Person.create_date,
            Person.email,
            Person.level
        ).order_by(sort_row.asc()).\
            filter(Person.remove_date.is_(None)).paginate(page, on_page, False)
        persons_return = [self.__make_dict(i) for i in persons_from_db.items]
        return persons_return

    def delete(self, id: int) -> bool:
        try:
            person = Person.query.filter_by(id=id, remove_date=None).first()
            if person:
                Person.query.filter_by(id=id).update(
                    {'remove_date': datetime.utcnow()})
                db.session.commit()
                return True
            return False
        except Exception as e:
            raise PersonException(e)

    def set_skill(self, id_person, id_skill):
        try:
            person = Person.query.filter_by(id=id_person, remove_date=None).first()
            skill = SkillService().get_by_id(id=id_skill)
            if person and skill:
                ps = person_skills.insert().values(person_id=person.id,
                                                    skill_id=skill.id)
        except Exception as e:
            raise PersonException(e)


    def check_person(self, id: int) -> bool:
        try:
            person = Person.query.filter_by(id=id, remove_date=None).first()
            if person:
                return True
            return False
        except:
            return False

    
    def update_skill_point(self, person_id: int, added_points: int):
        person = Person.query.filter_by(id=person_id, remove_date=None).first()
        skill_point = person.skill_point
        skill_point += added_points
        points = self.__check_level(skill_point, person.level)
        if points:
            person.level = person.level + 1
            person.skill_point = points
            return 1
        person.skill_point = skill_point
        return 0

    
    def __check_level(self, skill_point: int, level: int):
        import math
        point_for_level = Config.LEVEL_CONSTANT * level * math.sqrt(level * 100)
        if skill_point >=  point_for_level:
            return skill_point - point_for_level
        return False

    def __make_dict(self, row) -> dict:
        return {
            'id': row[0],
            'first_name': row[1],
            'second_name': row[2],
            'phone_number': row[3],
            'create_date': row[4],
            'email': row[5],
            'level': row[6]
        }
