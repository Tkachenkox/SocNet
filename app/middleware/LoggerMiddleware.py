import io
import logging
import os
import json
from uuid import uuid4
from flask import current_app, Flask
from werkzeug.wrappers import Request


class LoggerMiddleware(object):

    def __init__(self, app: Flask, logger: logging):
        self.app = app
        self.logging_level = logging.getLevelName('INFO')
        self.logger = logger
        self.uuid = None

    def __call__(self, enviroment, start_response):
        self.uuid = uuid4()
        request = Request(enviroment)
        body = request.stream.read()
        enviroment['wsgi.input'] = io.BytesIO(body)
        message_log = f'''Process UUID: {self.uuid} 
                        HTTP method: {str(request.method)} 
                        URL: {str(request.url)} 
                        Headers: {str(request.headers)}'''
        if request.args:
            message_log += f'Params: {request.args}'
        if body:
            if 'multipart/form-data' in request.headers.get_all('Content-Type')[0]:
                trimmed_body = body[body.index(b'{"first_name"'):]
                message_log += f'\nBody: {trimmed_body.decode("utf-8")}'
            else:
                message_log += f'\nBody: {body.decode("utf-8")}'
        self.logger.log(level=self.logging_level,
                        msg=message_log)

        def _start_response(status, headers, *args):
            self.logger.log(level=self.logging_level,
                            msg=f'''Process UUID:{self.uuid} 
                                HTTP status:{status} 
                                Headers:{headers}''')
            return start_response(status, headers, *args)

        return self.app(enviroment, _start_response)
