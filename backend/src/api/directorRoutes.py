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


@bp.route('/allNames', methods=['GET'])
def getNames() -> Response:
    directors = DirectorRepository().getAllDirectors()

    # if no matches are found, return 204
    if not directors:
        return Response(status=204)

    # convert list of dictionaries
    directors_dicts = [director.toDict() for director in directors]

    # return JSON response
    return jsonify(directors_dicts)
