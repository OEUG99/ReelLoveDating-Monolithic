from backend.src.repositories.MovieRepository import MovieRepository
from flask import Blueprint, request, Response, jsonify
from backend.src.models.Movie import Movie

bp = Blueprint('movie', __name__, url_prefix='/api/movie')

@bp.route('/<movieID>', methods=['GET'])
def getMovie(movieID: str) -> Response:
    output = MovieRepository().get(movieID)

    # if no user is found, return 204
    if output is None:
        return Response(status=204)

    return Response(output.toJSON(), status=200)

@bp.route('/getall', methods=['GET'])
def getAllMovies() -> Response:
    output = MovieRepository().getAll()


    # if no user is found, return 204
    if output is None:
        return Response(status=204)

    return jsonify(output), 200
