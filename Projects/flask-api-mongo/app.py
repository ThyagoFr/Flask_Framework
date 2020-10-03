from flask import Flask
from database.db import initialize_db
from routes import initialize_routes

app = Flask(__name__)
app.config.from_pyfile("./config.cfg")
initialize_db(app)
initialize_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
