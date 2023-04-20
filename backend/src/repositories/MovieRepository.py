from PyDataOpsKit import AbstractRepository
from backend.src.models.Movie import Movie


class MovieRepository(AbstractRepository):
    """
    This class is responsible for handling all database operations related to the Movie model.
    """

    def createTable(self):
        """
        Creates the table in the database if it does not exist.
        :return:
        :rtype:
        """
        try:
            self.db.query("""
                CREATE TABLE IF NOT EXISTS movies (
                    movieID VARCHAR(255) PRIMARY KEY,
                    name VARCHAR(255),
                    published_data VARCHAR(255),
                    director VARCHAR(255),
                    genre VARCHAR(255),
                    description VARCHAR(255),
                    rating VARCHAR(255)
                    )
                """)
            print("Movie table created successfully")
        except Exception as e:
            print("Error while creating the 'movies' table:", e)

    def add(self, movie: Movie):
        """
        Adds a movie to the database
        :param movie:
        :type movie:
        :return:
        :rtype:
        """
        addSQL = """
        INSERT INTO movies (movieID, name, publishedDate, director, genre, description, rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        self.db.query(addSQL, (movie.movieID,
                               movie.name,
                               movie.publishedDate,
                               movie.director,
                               movie.genre,
                               movie.description,
                               movie.rating))

    def update(self, obj):
        """
        Updates a movie in the database, returns the updated Movie object
        :param obj:
        :type obj:
        :return:
        :rtype:
        """
        pass

    def delete(self, movie):
        """
        Deletes a movie from the database
        :param movie:
        :type movie:
        :return:
        :rtype:
        """
        deleteSQL = """
        DELETE FROM movies WHERE movieID = %s
        """
        self.db.query(deleteSQL, (movie.movieID,))

    def get(self, movieID):
        """
        Gets a movie from the database via its ID
        :param movieID:
        :type movieID:
        :return:
        :rtype:
        """
        getSQL = """
        SELECT * FROM movies WHERE movieID = %s
        """

        movieTuple = self.db.query(getSQL, (movieID,))[0]

        if movieTuple:
            return Movie(movieID=movieTuple[0],
                         name=movieTuple[1],
                         publishedDate=movieTuple[2],
                         director=movieTuple[3],
                         genre=movieTuple[4],
                         description=movieTuple[5],
                         rating=movieTuple[6])
        else:
            return None

    def getAll(self):
        """
        Gets all movies from the database
        :return:
        :rtype:
        """
        pass

    def getList(self, limit, offset=None):
        pass

    def getCount(self):
        pass

    def getByAttribute(self, attribute):
        pass
