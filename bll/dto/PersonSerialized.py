from dal import Person

class PersonSerialized:

    def __init__(self, person: Person):
        self.data = {
            'first_name': person.first_name,
            'second_name': person.second_name,
            'last_name': person.last_name,
            'birthday': person.birthday,
            'email': person.email,
            'level': person.level,
            'skill_points': person.skill_point,
            'position': person.position,
            'recruit_date': person.recruit_date
        }