import uuid
from dataclasses import dataclass
from PyDataOpsKit import AbstractModel

from backend.src.models import Director, Actor


@dataclass
class Movie(AbstractModel):
    """
    This movie class models the movie entity in the database.
    Whenever we get a movie info from the database, we will create a movie object.
    Whenever we want to create a new movie, we will create a movie object, and then add it to the database
    via the movieRepository.
    """

    def __init__(self, name: str = None, publishedDate: str = None, director: Director = None, leadActor: Actor = None,
                 genre: str = None, description: str = None, rating: int = None, id: str = None):
        """
        creates a new movie object
        :param id:
        :type id:
        :param name:
        :type name:
        :param publishedDate:
        :type publishedDate:
        :param directorID:
        :type directorID:
        :param genre:
        :type genre:
        """


        if id is None:
            id = str(uuid.uuid4())

        self.id = id
        self.name = name
        self.publishedDate = publishedDate
        self.director = director
        self.leadActor = leadActor
        self.genre = genre
        self.description = description
        self.rating = rating

    def toDict(self) -> dict:
        """
        Converts the user object to a dictionary.
        :return:
        :rtype:
        """
        return {
            "id": self.id,
            "name": self.name,
            "publishedDate": self.publishedDate
        }

    def __repr__(self):
        return self.id
