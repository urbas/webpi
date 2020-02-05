from typing import Dict
import flask_login
from flask import Flask
from webpi.api.v1 import auth, health
from webpi.users import user_loader


def create_app(config: Dict = None):
    app = Flask(__name__)
    app.secret_key = "super secret secret"
    app.register_blueprint(auth.API)
    app.register_blueprint(health.API)
    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)
    login_manager.user_loader(user_loader)
    app.config.update(config or {})
    return app


def test_client(config: Dict = None):
    return create_app(config).test_client()
