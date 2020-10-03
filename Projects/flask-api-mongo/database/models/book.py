from ..db import db


class Books(db.Document):
    name = db.StringField(required=True)
    date = db.StringField(required=True)
