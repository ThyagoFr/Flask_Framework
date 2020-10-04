from flask import Blueprint, Response, request
from flask_jwt_extended import jwt_required
from services.writer_service import WriterService

writers_bp = Blueprint("writers", __name__)


@writers_bp.route("/writers")
@jwt_required
def all():
    writers = WriterService.all()
    return Response(writers, mimetype="application/json", status=200)


@writers_bp.route("/writers", methods=["POST"])
@jwt_required
def store():
    WriterService.store(request.json)
    return Response(status=201)
