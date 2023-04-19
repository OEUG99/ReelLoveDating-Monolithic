from flask import Blueprint, request, Response

from backend.src.models.Profile import Profile
from backend.src.models.User import User
from backend.src.repositories.ProfileRepository import ProfileRepository
from backend.src.repositories.UserRepository import UserRepository
from backend.src.utilities import generateToken, decodeToken

bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@bp.route('/register', methods=['POST'])
def register() -> Response:
    """ The register endpoint is used to create a new user in the database and an empty Profile for the user.
    :return: HTTP Response
    :rtype: Response
    """
    status_code = 400
    data = request.get_json()
    username = data.get('email')
    raw_password = data.get('password')

    # validating the username and password exist & formatted properly
    if not (username and raw_password):
        print('Invalid username or password')
        return Response(status=status_code)

    # Checking if the username is already taken
    if UserRepository().getByUsername(username):
        return Response(response="Username already taken",
                        status=status_code)

    try:
        # Creating the user in the DB
        user = User(username, raw_password)
        UserRepository().add(user)

        # Creating the profile for the user.
        profile = Profile(user.id)
        ProfileRepository().add(profile)

        token = generateToken(user)
        status_code = 200
        return Response(response=token,
                        status=status_code)
    except ValueError as e:
        return Response(response=str(e),
                        status=status_code)


@bp.route('/login', methods=['POST'])
def login() -> Response:
    """The login endpoint is used to authenticate a user and return a JWT token.
    :return: HTTP Response
    :rtype: Response
    """
    status_code = 400
    data = request.get_json()
    username = data.get('username')
    raw_password = data.get('password')

    # validating the username and password exist & formatted properly
    if not (username and raw_password):
        print('Invalid username or password')
        return Response(status=status_code)

    # Check if the user exists in the database
    user = UserRepository().getByUsername(username)

    if not user:
        return Response(response="Invalid username or password",
                        status=status_code)

    # Check if the password is correct
    hashed_password = user.password
    if not UserRepository().checkPassword(username, hashed_password):
        return Response(response="Invalid username or password",
                        status=status_code)
    try:
        token = generateToken(user)
        status_code = 200
        return Response(response=token,
                        status=status_code)
    except ValueError as e:
        return Response(response=str(e),
                        status=status_code)


@bp.route('/validate', methods=['POST'])
def validate() -> Response:
    """ The validate endpoint is used to validate a JWT token.
    :return: HTTP Response
    :rtype: Response
    """
    data = request.get_json()
    token = data.get('token')

    # validating the token exists
    if not token:
        return Response(status=400)

    # Decoding and validating the token
    try:
        decodedToken = decodeToken(token)

        if isinstance(decodedToken, Response):
            # if decode fails, we will return the Result object it creates.
            return decodedToken

        # if decode is a success it will return a string containing the token.
        return Response(response=f"your access to user {decodedToken.get('userID')} is valid", status=200)
    except Exception as e:
        return Response(response=str(e), status=400)
