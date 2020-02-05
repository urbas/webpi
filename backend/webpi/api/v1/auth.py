from flask import Blueprint, request, abort
from flask.json import jsonify
from flask_login import login_required, current_user, logout_user
from webpi import users

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

    user = users.auth_user(email, password)
    if user is None:
        return abort(400)
    return jsonify({})


@API.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return jsonify({})
