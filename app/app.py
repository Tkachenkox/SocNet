from flask import Flask
from config import Config
from .BlueprintGroup import BlueprintGroup
from controller import test_blueprint, person_blueprint, skill_blueprint
import logging
import logging.handlers
from .middleware import LoggerMiddleware


def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    logger = create_logger(config)
    BlueprintGroup('api', test_blueprint, person_blueprint, skill_blueprint).register_blueprints(app)
    app.wsgi_app = LoggerMiddleware(app.wsgi_app, logger)
    return app


def create_logger(config: Config):
    logger = logging.getLogger(__name__)
    logger.setLevel("INFO")
    #formatter = logging.Formatter(config.LOGGER_FROMATTER)
    formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")
    #handler = logging.handlers.RotatingFileHandler(
    #        config.LOG_PATH,
    #        maxBytes=1024 * 1024) 
    handler = logging.handlers.RotatingFileHandler(
            "app.log",
            maxBytes=1024 * 1024)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
