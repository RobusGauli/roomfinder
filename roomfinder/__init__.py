from flask import Flask 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('postgres://user:postgres@localhost:5432/roomfi')


def create_app():
    app = Flask(__name__)
    from roomfinder.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    return app


