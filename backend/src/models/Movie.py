from PyDataOpsKit import AbstractModel


class Movie(AbstractModel):
    """
    This movie class models the movie entity in the database.
    Whenever we get a movie info from the database, we will create a movie object.
    Whenever we want to create a new movie, we will create a movie object, and then add it to the database
    via the movieRepository.
    """

    def __init__(self, movieID: str, name: str = None, publishedDate: str = None, director: str = None,
                 genre: str = None, description: str = None, rating: int = None):
        """
        creates a new movie object
        :param movieID:
        :type movieID:
        :param name:
        :type name:
        :param publishedDate:
        :type publishedDate:
        :param director:
        :type director:
        :param genre:
        :type genre:
        """
        self.movieID = movieID
        self.name = name
        self.publishedDate = publishedDate
        self.director = director
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
            "movieID": self.movieID,
            "name": self.name,
            "published_date": self.publishedDate,
            "director": self.director,
            "genre": self.genre
        }