from flask import Blueprint
from flask.json import jsonify

API = Blueprint("health", __name__, url_prefix="/api/v1/health")


@API.route("")
def get():
    return jsonify(healthy=True)
