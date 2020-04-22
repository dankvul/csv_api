from flask import Flask
from config import Config
from .api import api


def getApp():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(api)
    return app
