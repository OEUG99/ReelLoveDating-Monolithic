from flask import Blueprint, request, Response
from backend.src.services.MovieDiscoveryService import MovieDiscovery

bp = Blueprint('auth', __name__, url_prefix='/api/admin')


@bp.route('/updateMovies', methods=['POST'])
def updateMovies() -> Response:
    # todo: add authentication to this endpoint ensuring only admins can access it.
    try:
        MovieDiscoveryService().updateMovies()
        return Response(status=200)
    except Exception as e:
        return Response(response=str(e), status=400)




