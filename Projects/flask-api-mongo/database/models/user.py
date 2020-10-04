from ..db import db


class Users(db.Document):
    email = db.StringField(required=True)
    password = db.StringField(required=True)