from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from routes import initialize_routes


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("./config.cfg")
    CORS(app)
    JWTManager(app)
    initialize_db(app)
    initialize_routes(app)
    return app


if __name__ == "__main__":
    application = create_app()
    application.run(debug=True)
