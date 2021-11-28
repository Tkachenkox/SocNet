import json

from bll.TestService import TestService
from flask import Blueprint, Response, current_app, jsonify, request

from .Dto import TestCreateDto, TestUpdateDto
from .TokenHelper import token_required

test_blueprint = Blueprint("test_blueprint", __name__, url_prefix="test")

@test_blueprint.route("/", methods = ['POST'])
def add() -> Response:
    try:
        id = token_required(request, need_current_user_id=True)
        data = request.json
        dto = TestCreateDto(data, id)
        result = TestService().add(dto.data)
        if type(result) is int:
            return jsonify({'success': f'added test with id {result}'}), 200
        return jsonify({'error': result}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@test_blueprint.route("/<int:id>", methods = ['GET'])
def get_by_id(id: int) -> Response:
    try:
        token_required(request)
        test = TestService().get_by_id(id)
        if test:
            return jsonify({'success': test}), 200
        else:
            return jsonify({'error': 'test not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@test_blueprint.route("/", methods = ['GET'])
def get() -> Response:
    try:
        token_required(request)
        page = request.args.get('page', 1, type=int)
        on_page = request.args.get('on_page', int(
            current_app.config['PERSONS_PER_PAGE']), type=int)
        sort_by = request.args.get('sort_by', 'name', type=str)
        result = TestService().get_all(page=page, on_page=on_page, sort_by=sort_by)
        if result:
            return jsonify({'tests': result}), 200
        return jsonify({'error': 'no tests yet'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@test_blueprint.route("/<int:id>", methods = ['PUT'])
def update(id: int) -> Response:
    try:
        id = token_required(request, need_current_user_id=True)
        data = request.json
        if data:
            dto = TestUpdateDto(data)
            result = TestService().update(id, dto.data)
            if type(result) is bool:
                return jsonify({'success': 'test updated'}), 200
            return jsonify({'error': result}), 400
    except Exception as e:
        return jsonify({'error': e}), 400

@test_blueprint.route("/<int:id>", methods = ['DELETE'])
def delete(id: int) -> Response:
    try:
        creator_id = token_required(request, need_current_user_id=True)
        if TestService().delete(id, creator_id):
            return jsonify({'success': 'test deleted'}), 200
        return jsonify({'error': 'test not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@test_blueprint.route("/start/<int:id>", methods = ['GET'])
def start_test(id: int) -> Response:
    try:
        person_id = token_required(request, need_current_user_id=True)
        test = TestService().start_test(id, person_id)
        if test:
            return jsonify({'success': test}), 200
        return jsonify({'error': 'test not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@test_blueprint.route("/check_result/<int:id_test>", methods = ['POST'])
def check_result(id_test: int) -> Response:
    try:
        data = request.json
        id_person = token_required(request, need_current_user_id=True)
        result, points = TestService().check_result(id_test, id_person, data)
        if result:
            return jsonify({'result': f'{points} point(s) and earned next level!'}), 200
        return jsonify({'result': f'{points} point(s)'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
