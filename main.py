from flask_migrate import Migrate

from app import create_app
from config import Config
from dal import db, Person, Test, WorkExperience, Skill, TestResult

config = Config()
app = create_app(Config)
db.init_app(app)
migrate = Migrate(app, db)
