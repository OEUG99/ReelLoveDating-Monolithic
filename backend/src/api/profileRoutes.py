from flask import Blueprint, request

from backend.src.models.Profile import Profile
from backend.src.repositories.ProfileRepository import ProfileRepository
from backend.src.utilities import decodeToken

bp = Blueprint('profile', __name__, url_prefix='/api/profile')


@bp.route('/create', methods=['POST'])
def createProfile():
    data = request.get_json()
    authToken = data.get('authToken')

    decodedToken = decodeToken(authToken)

    # todo updates these to be Response objects
    if decodedToken == "Token expired.":
        return "Token expired."
    elif decodedToken == "Invalid token.":
        return "Invalid token."

    profile = Profile(decodedToken["user_id"])

    ProfileRepository().add(profile)

    return "Profile created."


# get profile by ID now via URL
@bp.route('/<userID>', methods=['GET'])
def getProfile(userID):
    print(userID)
    output = ProfileRepository().get_by_userID(userID)
    print(output)
    return str(output)



@bp.route('/random', methods=['POST'])
def getRandomProfiles():
    # TODO: added some security checks so that only logged in users can access this endpoint
    # TODO: add a limit to the number of profiles that can be fetched at once
    # ADD A COOL DOWN PERIOD TO PREVENT SPAMMING
    # data = request.get_json()
    # numProfilesToFetch = data.get('numProfilesToFetch')
    print("Fetching random profiles...")

    profiles = ProfileRepository().get_by_userID()
    print(profiles)
    return str(profiles)


@bp.route('/health', methods=['GET'])
def health():
    return "OK"
