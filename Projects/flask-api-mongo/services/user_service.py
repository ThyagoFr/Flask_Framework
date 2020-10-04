from database.models.user import Users
from flask_mongoengine import DoesNotExist
from handler.handler import HandlerException
from flask_jwt_extended import create_access_token
from flask import jsonify


class UserService:
    @staticmethod
    def store(data):
        user = Users(**data)
        user.save()

    @staticmethod
    def all():
        users = Users.objects().to_json()
        return users

    @staticmethod
    def auth(data):
        email = data["email"]
        password = data["password"]
        try:
            user = Users.objects.get(email=email)
            if user.password != password:
                raise HandlerException(message="Check your credentials", status=401)
        except DoesNotExist:
            raise HandlerException(message="User not found", status=404)
        return jsonify({"token": create_access_token(identity=user.email)})
