from views.writer_view import writers_bp
from views.book_view import book_bp
from views.auth_view import auth_bp
from handler.handler import errors_bp


def initialize_routes(app):
    app.register_blueprint(writers_bp)
    app.register_blueprint(book_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(errors_bp)
