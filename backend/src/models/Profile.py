import json
from dataclasses import dataclass
from PyDataOpsKit import AbstractModel


@dataclass
class Profile(AbstractModel):

    def __init__(self,
                 userID,
                 visibility=False,
                 firstName=None,
                 lastName=None,
                 bio=None,
                 gender=None,
                 age=None,
                 location=None,
                 sexuality=None,
                 interests=None,
                 favoriteMovies=None):
        self.userID = userID
        self.visibility = visibility
        self.firstName = firstName
        self.lastName = lastName
        self.bio = bio
        self.gender = gender
        self.age = age
        self.location = location
        self.sexuality = sexuality
        self.interests = interests
        self.favoriteMovies = favoriteMovies

    def toDict(self) -> dict:
        return {
            "userID": self.userID,
            "visibility": self.visibility,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "bio": self.bio,
            "gender": self.gender,
            "age": self.age,
            "location": self.location,
            "sexuality": self.sexuality,
            "interests": self.interests,
            "favoriteMovies": self.favoriteMovies
        }

    def toJSON(self):
        return json.dumps(self.toDict())
