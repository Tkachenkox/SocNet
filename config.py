import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def get_env(key: str) -> str:
    return os.environ[key]


def get_db_uri() -> str:
    return f"{get_env('DB_DRIVER')}://{get_env('POSTGRES_USER')}:{get_env('POSTGRES_PASSWORD')}@{get_env('POSTGRES_HOST')}/{get_env('POSTGRES_DB')}?options=-c+timezone%3Dutc"

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = get_env('SQLALCHEMY_TRACK_MODIFICATIONS')
    SECRET_KEY = get_env('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = get_db_uri()
