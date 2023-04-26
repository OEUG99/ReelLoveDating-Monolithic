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