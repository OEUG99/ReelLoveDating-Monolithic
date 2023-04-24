import json
from dataclasses import dataclass
from PyDataOpsKit import AbstractModel


@dataclass
class Profile(AbstractModel):
    """
    This Profile class models the Profile entity in the database.
    Whenever we get a Profile info from the database, we will create a Profile object.
    Whenever we want to create a new Profile, we will create a Profile object, and then add it to the database
    via the ProfileRepository.
    """

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
                 favoriteMovies=None,
                 favoriteActor=None,
                 favoriteDirector=None):
        """
        creates a new Profile object
        :param userID:
        :type userID:
        :param visibility:
        :type visibility:
        :param firstName:
        :type firstName:
        :param lastName:
        :type lastName:
        :param bio:
        :type bio:
        :param gender:
        :type gender:
        :param age:
        :type age:
        :param location:
        :type location:
        :param sexuality:
        :type sexuality:
        :param interests:
        :type interests:
        :param favoriteMovies:
        :type favoriteMovies:
        """
        self.id = userID
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
        self.favoriteActor = favoriteActor
        self.favoriteDirector = favoriteDirector

    def toDict(self) -> dict:
        """
        converts the Profile object to a dictionary
        :return:
        :rtype:
        """
        return {
            "id": self.id,
            "visibility": self.visibility,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "bio": self.bio,
            "gender": self.gender,
            "age": self.age,
            "location": self.location,
            "sexuality": self.sexuality,
            "interests": self.interests,
            "favoriteMovies": self.favoriteMovies,
            "favoriteActor": self.favoriteActor,
            "favoriteDirector": self.favoriteDirector
        }
