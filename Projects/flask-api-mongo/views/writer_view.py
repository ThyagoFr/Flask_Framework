from flask import Blueprint, Response, request
from services.writer_service import WriterService

writers_bp = Blueprint("writers", __name__)


@writers_bp.route("/writers")
def all():
    writers = WriterService.all()
    return Response(writers, mimetype="application/json", status=200)


@writers_bp.route("/writers", methods=["POST"])
def store():
    WriterService.store(request.json)
    return Response(status=201)
