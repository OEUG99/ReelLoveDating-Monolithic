from flask import Blueprint, request, Response, jsonify
from backend.src.models.Match import Match
from backend.src.repositories.MatchRepository import MatchRepository
from backend.src.utilities import decodeToken

bp = Blueprint('match', __name__, url_prefix='/api/match')


@bp.route('/add', methods=['POST'])
def addMatch() -> Response:
    """The add endpoint is used to add a match in the database
   :return: HTTP Response
   :rtype: Response
   """
    # decode token first
    data = request.get_json()
    token = data.get('token')
    decoded_token = decodeToken(token)
    userID = decoded_token['userID']
    secondUserID = data.get('secondUserID')

    try:
        match = Match(userID, secondUserID)
        MatchRepository().add(match)
        return Response(status=200)
    except ValueError as e:
        return Response(response=str(e),
                        status=400)


@bp.route('/allMatches', methods=['GET'])
def getAllMatches() -> Response:
    matches = MatchRepository().getAll()

    # if no matches are found, return 204
    if not matches:
        return Response(status=204)

    # convert matches to list of dictionaries
    matches_dicts = [match.toDict() for match in matches]

    # return JSON response
    return jsonify(matches_dicts)
