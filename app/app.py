from flask import Flask
from config import Config
from .BlueprintGroup import BlueprintGroup


def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    BlueprintGroup('api', None).register_blueprints(app)
    return app