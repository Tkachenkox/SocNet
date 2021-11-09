from typing import cast
from bll import PersonService
from .Dto import PersonAuthDataDto, PersonDataDto, PersonUpdateDto
from flask import Blueprint, Response, current_app, jsonify, request

from .TokenHelper import token_required

person_blueprint = Blueprint("person_blueprint", __name__, url_prefix="person")

@person_blueprint.route('/login', methods=['POST'])
def login() -> Response:
    data = request.json
    print(data)
    dto = PersonAuthDataDto(
        email = data['email'],
        password = data['password']
    )
    result = PersonService().auth(data = dto.data)
    if result:
        return jsonify({'status':f'{result}'}), 200
    else:
        return jsonify({'status':'unauthorized'}), 401


@person_blueprint.route('/', methods=['POST'])
def create() -> Response:
    token_required(request, need_admin=True)
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

    try:
        result = PersonService().create(dto.data)
        return jsonify({'status':'id'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@person_blueprint.route('/', methods=['GET'])
def get_all():
    page = request.args.get('page', 1, type=int)
    on_page = request.args.get('on_page', int(
        current_app.config['PERSONS_PER_PAGE']), type=int)
    sort_type = request.args.get('sort_by', 'name', type=str)

    response = PersonService().get_all(sort_type, page, on_page)
    return jsonify({'persons': response}), 200


@person_blueprint.route('/<int:id>', methods=['GET'])
def get_by_id(id: int) -> Response:
    person_data = PersonService().get_by_id(id)
    if person_data:
        return jsonify({'person': person_data}), 200
    return jsonify({'error': f'Person with id {id} not found'}), 404

@person_blueprint.route('/<int:id>', methods=['PUT'])
def update_by_id(id: int) -> Response:
    token_required(request)
    data = request.json
    dto = PersonUpdateDto(
        name=data.get('name'),
        second_name = data.get('second_name'),
        last_name = data.get('last_name'),
        birtday = data.get('birtday'),
        phone_number = data.get('phone_number'),
        email = data.get('email'),
        gender = data.get('gender'),
        password = data.get('password'),
    )
    PersonService.update(id, dto.data)

@person_blueprint.route('/<int:id>', methods=['DELETE'])
def delete(id) -> Response:
    try:
        result = PersonService().delete(id)
        if result:
            return jsonify({'status': 'Success'}), 200
        return jsonify({'error': 'Person not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@person_blueprint.route('/addSkill/<int:id_person>/<int:id_skill>', methods=['POST'])
def set_skill(id_person, id_skill) -> Response:
    try:
        result = PersonService().set_skill(id_person=id_person, id_skill=id_skill)
        if result:
            return jsonify({'status': 'success'}), 200
        return jsonify({'error': 'skill or person not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

