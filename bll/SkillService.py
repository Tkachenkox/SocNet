from dal import Skill, db
from app.exceptions import SkillException
from datetime import datetime

class SkillService:

    def get_by_id(self, id: int):
        try:
            skill = Skill.query.filter_by(id=id, remove_date=None).first()
            if skill:
                return {
                    'id': skill.id,
                    'name': skill.name
                }
            return None
        except Exception as e:
            raise SkillException(str(e))
            

    def get_all(self, page: int, on_page: int) -> dict:
        try:
            skills =  db.session.query(
                Skill.id,
                Skill.name).order_by(Skill.name.asc()).\
                filter(Skill.remove_date.is_(None)).paginate(page, on_page, False)
            skills_return = [self.__make_dict(i) for i in skills.items]
            return skills_return
        except Exception as e:
            raise SkillException(str(e))

    def add(self, data: dict) -> int:
        try:
            if data['name']:
                new_skill = Skill(name=data['name'])
                db.session.add(new_skill)
                db.session.commit()
                return new_skill.id
            return None
        except Exception as e:
            print(e)
            raise SkillException(str(e))

    def delete(self, id: int) -> bool:
        try:
            if id:
                skill = Skill.query.filter_by(id=id, remove_date=None).first()
                if skill:
                    Skill.query.filter_by(id=id).update(
                            {'remove_date': datetime.utcnow()})
                    db.session.commit()
                    return True
                return False
            return None
        except Exception as e:
            raise SkillException(str(e))

    def __make_dict(self, row: list) -> dict:
        return {
            'id': row[0],
            'name': row[1]
        }