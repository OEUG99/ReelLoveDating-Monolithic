import uuid
from dataclasses import dataclass
from PyDataOpsKit.AbstractModel import AbstractModel


@dataclass
class Director(AbstractModel):
    """
    This Director class models the Director entity in the database.
    Whenever we get a Director info from the database, we will create a Director object.
    Whenever we want to create a new Director, we will create a Director object, and then add it to the database
    via the DirectorRepository.
    """
    def __init__(self, directorID=None, firstName=None, lastName=None, directedMovie=None, directedInGenre=None,
                 isFavoriteOf=None):
        self.id = directorID or str(uuid.uuid4())    # if directorID is None, then generate a new one and assign new uuid
        self.firstName = firstName
        self.lastName = lastName
        self.directedMovie = directedMovie
        self.directedInGenre = directedInGenre  # todo: this may not be needed, duplicate data in movie table.
        self.isFavoriteOf = isFavoriteOf

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "directedMovie": self.directedMovie,
            "directedInGenre": self.directedInGenre,
            "isFavoriteOf": self.isFavoriteOf
        }

    def __repr__(self):
        return self.id
