from ..db import db


class Writers(db.Document):
    name = db.StringField(required=True)
