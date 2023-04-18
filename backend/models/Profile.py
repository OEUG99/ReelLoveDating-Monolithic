from dataclasses import dataclass
from PyDataOpsKit import AbstractEntity


@dataclass
class Profile(AbstractEntity):

    def __init__(self, userID):
        self.userID = userID
        self.visibility = False
        self.firstName = None
        self.lastName = None
        self.bio = None
        self.gender = None
        self.age = None
        self.location = None
        self.sexuality = None
        self.interests = None
        self.favoriteMovies = None

    def __str__(self):
        return f"{self.userID} - {self.visibility}"
