
from functools import wraps

import jwt
from app.exceptions import TokenException
from config import Config
from dal.models import Person, Role
from flask import jsonify, request
from flask.globals import current_app


def token_required(request: request, 
                    need_admin: bool = False, 
                    need_superuser: bool = False,
                    need_current_user_id: bool = False):
    token = None
    if 'Authorization' in request.headers:
        token = request.headers['Authorization']
    if not token:
        raise TokenException('Token is missing')
    try:
        data = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        current_user = Person.query.filter_by(id=data['id'], remove_date=None).first() 
        if need_admin:
            role = Role.query.filter_by(id=current_user.role_id).first()
            if role.is_admin:
                pass
            else:
                raise TokenException("Need admin permission")

        if need_superuser:
            role = Role.query.filter_by(id=current_user.role_id).first()
            if role.is_superuser:
                pass
            else:
                raise TokenException('Need superuser permission !!')

        if need_current_user_id:
            return current_user.id
    except Exception as e:
        print(e)
        raise TokenException(str(e))

