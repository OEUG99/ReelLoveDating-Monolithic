from flask import Blueprint, request, Response
from backend.src.models.Like import Like
from backend.src.repositories.LikeRepository import LikeRepository

bp = Blueprint('like', __name__, url_prefix='/api/like')


@bp.route('/add', methods=['POST'])
def addLike() -> Response:
    """The add endpoint is used to add a like in the database
    :return: HTTP Response
    :rtype: Response
    """
    data = request.get_json()
    userID = data.get('userID')
    secondaryUserID = data.get('secondaryUserID')

    like = Like(userID=userID, secondaryUserID=secondaryUserID)
    LikeRepository().add(like)

    return Response(status=200)