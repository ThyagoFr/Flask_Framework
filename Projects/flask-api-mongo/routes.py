from views.writer_view import writers_bp
from views.book_view import book_bp
from handler.handler import errors_bp


def initialize_routes(app):
    app.register_blueprint(writers_bp)
    app.register_blueprint(book_bp)
    app.register_blueprint(errors_bp)
