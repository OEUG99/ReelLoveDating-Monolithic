from dataclasses import dataclass
from PyDataOpsKit import AbstractModel


@dataclass
class Genre(AbstractModel):
    """
    this Genre class models the Genre entity in the database.
    Whenever we get a Genre info from the database, we will create a Genre object.
    Whenever we want to create a new Genre, we will create a Genre object, and then add it to the database
    via the GenreRepository.
    """

    def __init__(self, genreName, actedInGenre=None, belongsToGenre=None, hasDirectedGenre=None, isFavoriteOf=None):
        self.genreName = genreName
        self.actedInGenre = actedInGenre  # todo: may not be needed, duplicate data in movie table.
        self.belongsToGenre = belongsToGenre
        self.hasDirectedGenre = hasDirectedGenre  # not sure why this is in the schema?
        self.isFavoriteOf = isFavoriteOf

    def toDict(self) -> dict:
        return {
            "genreName": self.genreName,
            "actedInGenre": self.actedInGenre,
            "belongsToGenre": self.belongsToGenre,
            "hasDirectedGenre": self.hasDirectedGenre,
            "isFavoriteOf": self.isFavoriteOf
        }
