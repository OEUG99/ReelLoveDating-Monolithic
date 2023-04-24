from flask import Blueprint, request, Response

from backend.src.models.Profile import Profile
from backend.src.repositories.ProfileRepository import ProfileRepository
from backend.src.utilities import decodeToken

bp = Blueprint('profile', __name__, url_prefix='/api/profile')


@bp.route('/create', methods=['POST'])
def createProfile() -> Response:
    data = request.get_json()
    decodedToken = decodeToken(data.get('authToken'))

    if isinstance(decodedToken, Response):
        return decodedToken

    profile = Profile(decodedToken["user_id"])

    ProfileRepository().add(profile)

    return Response(status=200)


@bp.route('/update', methods=['POST'])
def updateProfile() -> Response:
    data = request.get_json()
    decodedToken = decodeToken(data.get('authToken'))

    if isinstance(decodedToken, Response):
        return decodedToken

    # get profile by ID and updating it
    profile = Profile(decodedToken['user_id'])
    profile.firstName = data.get('firstName')
    profile.lastName = data.get('lastName')
    profile.bio = data.get('bio')
    profile.location = data.get('location')
    profile.visibility = data.get('visibility')
    profile.gender = data.get('gender')
    profile.age = data.get('age')
    profile.interests = data.get('interests')
    profile.sexuality = data.get('sexuality')
    profile.favoriteMovies = data.get('favoriteMovies')
    profile.favoriteActor = data.get('favoriteActor')
    profile.favoriteDirector = data.get('favoriteDirector')

    # updating profile in DB
    ProfileRepository().update(profile)

    return Response(status=200)


@bp.route('/<userID>', methods=['GET'])
def getProfile(userID: str) -> Response:
    output = ProfileRepository().getByUserID(userID)
    print(output.toJSON())

    # if no user is found, return 204
    if output is None:
        return Response(status=204)

    return Response(output.toJSON(), status=200)


@bp.route('/random', methods=['POST'])
def getRandomProfiles() -> Response:
    data = request.get_json()
    numProfilesToFetch = data.get('numProfilesToFetch')
    print("Fetching random profiles...")

    # security check limits the number of profiles that can be fetched at once
    if numProfilesToFetch > 20:
        numProfilesToFetch = 20

    profilesList = ProfileRepository().getRandom(numProfilesToFetch)

    if profilesList is None:
        return Response(status=204)

    return Response(profilesList, status=200)


@bp.route('/health', methods=['GET'])
def health():
    return "OK"
