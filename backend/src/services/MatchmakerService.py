from backend.src.models import Profile, Match, Like

from backend.src.repositories import LikeRepository
from backend.src.repositories import ProfileRepository
from backend.src.repositories import LikeRepository
class MatchmakerService:
    """
    This class is responsible for matching profiles to each other. It will run a matching algorithm on the profiles
    and will add any matches to the Match table in the database.
    """

    def getMatch(self, callingUser):
        """
        Gets all matches in the database
        """
        query = """
                    SELECT userID
                    FROM Like, (
                    SELECT userID, secondaryUserID
                    FROM Profile, Like
                    WHERE Profile.userID = Like.userID AND
                    Profile.userID = callingUser
                    ) AS Like2
                    WHERE Like2.secondaryUserID = Like.userID
               """


    def __init__(self):
        pass

