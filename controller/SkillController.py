from bll import SkillService
from flask import Blueprint, Response, current_app, jsonify, request

from .Dto import SkillCreateDto
from .TokenHelper import token_required

skill_blueprint = Blueprint('person_blueprint', __name__, url_prefix='skill')

@skill_blueprint.route('/<int:id>', methods=['GET'])
def get_by_id(id: int) -> Response:
    try:
        skill = SkillService().get_by_id(id)
        if skill:
            return jsonify({'skill': skill}), 200
        return jsonify({'error': 'skill not found'}), 404
    except Exception as e:
        return jsonify({'error': e}), 400

@skill_blueprint.route('/', methods=['GET'])
def get():
    try:
        page = request.args.get('page', 1, type=int)
        on_page = request.args.get('on_page', int(
        current_app.config['PERSONS_PER_PAGE']), type=int)
        skill = SkillService().get_all(page, on_page)
        if skill:
            return jsonify({'skills': skill}), 200
        return jsonify({'error': 'skills not found'}), 404
    except Exception as e:
        return jsonify({'error': e}), 400

@skill_blueprint.route('/', methods=['POST'])
def create():
    try:
        data = request.json
        dto = SkillCreateDto(name=data.get['name'])
        id = SkillService().add(data=dto.data)
        if id:
            return jsonify({'success': f'skill id {id}'})
        return jsonify({'error': 'Skill name not found'})
    except Exception as e:
        return jsonify({'error': e}), 400


@skill_blueprint.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    try:
        if SkillService().delete(id):
            return jsonify({'success': f'skill with id {id} deleted'})
        return jsonify({'error': 'skill not found'})
    except Exception as e:
        return jsonify({'error': e}), 400

