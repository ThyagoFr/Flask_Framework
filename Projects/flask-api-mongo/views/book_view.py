from flask import Blueprint, Response, request, jsonify
from database.models.book import Books
from handler.handler import HandlerException

book_bp = Blueprint("books", __name__)


@book_bp.route("/books")
def all():
    books = Books.objects().to_json()
    return Response(books, mimetype="application/json", status=200)


@book_bp.route("/books/<name>")
def find(name):
    book = Books.objects(name=name)
    if len(book) == 0:
        raise HandlerException(message="Book Not Found", status=404)


@book_bp.route("/books", methods=["POST"])
def store():
    data = request.json
    bk = Books(**data)
    bk.save()
    return Response(status=201)
