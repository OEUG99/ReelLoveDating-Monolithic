from backend.src.repositories.ActorRepository import ActorRepository
from flask import Blueprint, request, Response, jsonify
from backend.src.models.Actor import Actor

bp = Blueprint('actor', __name__, url_prefix='/api/actor')

@bp.route('/<actorID>', methods=['GET'])
def getActor(actorID: str) -> Response:
    output = ActorRepository().get(actorID)

    # if no user is found, return 204
    if output is None:
        return Response(status=204)

    return Response(output.toJSON(), status=200)

@bp.route('/allNames', methods=['GET'])
def getNames() -> Response:
    actors = ActorRepository().getAllActors()

    # if no matches are found, return 204
    if not actors:
        return Response(status=204)

    # convert list of dictionaries
    actors_dicts = [actor.toDict() for actor in actors]

    # return JSON response
    return jsonify(actors_dicts)