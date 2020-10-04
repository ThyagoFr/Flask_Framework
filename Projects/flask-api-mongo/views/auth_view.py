from flask import Blueprint, request
from services.user_service import UserService

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=['POST'])
def register():
    UserService.store(request.json)
    return '', 201


@auth_bp.route("/login", methods=['POST'])
def login():
    response = UserService.auth(request.json)
    return response, 200
