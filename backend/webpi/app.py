from flask import Flask
from webpi.api.v1 import health

APP = Flask(__name__)
APP.register_blueprint(health.API)


def test_client():
    return APP.test_client()
