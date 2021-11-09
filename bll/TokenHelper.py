from dal.models import Person
import jwt
from datetime import datetime, timedelta
from config import Config

def generate_token(person: Person):
    token = jwt.encode({
            'id': person.id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30),
            'role' : person.role_id
        }, 
        Config.SECRET_KEY,
        algorithm = "HS256")
    return token
