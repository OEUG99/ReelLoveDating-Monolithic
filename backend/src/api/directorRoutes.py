from backend.src.repositories.DirectorRepository import DirectorRepository
from flask import Blueprint, request, Response, jsonify
from backend.src.models.Director import Director

bp = Blueprint('director', __name__, url_prefix='/api/director')

@bp.route('/<directorID>', methods=['GET'])
def getDirector(directorID: str) -> Response:
    output = DirectorRepository().get(directorID)

    # if no user is found, return 204
    if output is None:
        return Response(status=204)

    return Response(output.toJSON(), status=200)