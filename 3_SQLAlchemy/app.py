from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("config.cfg")

db = SQLAlchemy(app)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),unique=True)
    password = db.Column(db.String(30))
    email = db.Column(db.String(30))
    join_date = db.Column(db.DateTime)
    orders = db.relationship("Order",backref="member",lazy="dynamic")

    def __repr__(self):
        return "<Member {}>".format(self.username)

class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    price = db.Column(db.Integer)
    member_id = db.Column(db.Integer,db.ForeignKey("member.id"))

    def __repr__(self):
        return "<Order {}>".format(self.price)

if __name__ == "__main__":
    app.run()