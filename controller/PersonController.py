from .Dto import PersonAuthDataDto, PersonDataDto
from flask import Blueprint, Request, Response, blueprint, jsonify

person_blueprint = Blueprint("person_blueprint", __name__, url_prefix="/person")

@person_blueprint.route('/login', methods=['POST'])
def login(request: Request) -> Response:
    data = request.data
    dto = PersonAuthDataDto(
        email = data['email'],
        phone_number = data['phone_number'],
        password=data['password']
    )
    return jsonify({'status':'success'}), 200

@person_blueprint.route('/', methods=['POST'])
def add(request: Request) -> Response:
    data = request.json
    dto = PersonDataDto(
        name=data['name'],
        last_name=data['last_name'],
        second_name=data['second_name'],
        birtday=data['birthday'],
        phone_number=data['phone_number'],
        email=data['email'],
        gender=data['gender'],
        password=data['password']
    )
    return jsonify({'status':'success'}), 200
