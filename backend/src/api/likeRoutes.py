from flask import Blueprint, request, Response
from backend.src.models.Like import Like
from backend.src.repositories.LikeRepository import LikeRepository
from backend.src.utilities import decodeToken

bp = Blueprint('like', __name__, url_prefix='/api/like')


@bp.route('/add', methods=['POST'])
def addLike() -> Response:
    """The add endpoint is used to add a like in the database
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
        like = Like(userID, secondUserID)
        LikeRepository().add(like)
        return Response(status=200)
    except ValueError as e:
        return Response(response=str(e),
                        status=400)
