from flask import Blueprint, request, abort, current_app
from flask.json import jsonify
from flask_login import login_required, current_user, login_user, logout_user
from webpi.users import User

API = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@API.route("/user")
@login_required
def get_user():
    return jsonify(email=current_user.email)


@API.route("/login", methods=["POST"])
def login():
    if request.json is None:
        return abort(400)

    email = request.json.get("email")
    password = request.json.get("password")
    if email is None or password is None:
        return abort(400)

    user = current_app.config.users.get(email)
    if user is None:
        return abort(400)

    if password != user.get("password"):
        return abort(400)

    login_user(User(email))
    return jsonify({})


@API.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return jsonify({})
