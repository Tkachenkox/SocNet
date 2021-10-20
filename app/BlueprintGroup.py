from flask import Flask

class BlueprintGroup:

    def __init__(self, url_prefix: str, *blueprints):
        self.url_prefix = url_prefix
        self.blueprints = blueprints

    def register_blueprints(self, app: Flask) -> Flask:
        for blueprint in self.blueprints:
            app.register_blueprint(blueprint, url_prfix=f"{self.url_prefix}/{blueprint.url_prefix}")