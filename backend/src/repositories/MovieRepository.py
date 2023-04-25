from PyDataOpsKit import AbstractRepository
from backend.src.models.Movie import Movie
from backend.src.repositories.DirectorRepository import DirectorRepository
from backend.src.repositories.ActorRepository import ActorRepository


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
                    id VARCHAR(255) PRIMARY KEY,
                    name VARCHAR(255),
                    publishedDate VARCHAR(255),
                    directorID VARCHAR(255),
                    leadActorID VARCHAR(255),
                    genre VARCHAR(255),
                    description VARCHAR(255),
                    rating VARCHAR(255)
                    )
                """)
            print("Profile table created successfully")
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
        self.db.query("""
        INSERT INTO movies (id, name, publishedDate, directorID, leadActorID, genre, description, rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (movie.id,
              movie.name,
              movie.publishedDate,
              movie.director.id,
              movie.leadActor.id,
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
        self.db.query(deleteSQL, (movie.id,))

    def get(self, movieID):
        """
        Gets a movie from the database via its ID
        :param movieID:
        :type movieID:
        :return:
        :rtype:
        """
        getSQL = """
        SELECT * FROM movies WHERE id = %s
        """

        movieTuple = self.db.query(getSQL, (movieID,))[0]

        print(movieTuple)

        if movieTuple:
            return Movie(id=movieTuple[0],
                         name=movieTuple[1],
                         publishedDate=movieTuple[2],
                         director=DirectorRepository().get(movieTuple[3]),
                         leadActor=ActorRepository().get(movieTuple[4]),
                         genre=movieTuple[5],
                         description=movieTuple[6],
                         rating=movieTuple[7])
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

    def getAllMovies(self):
        """
        Gets all movie from the database with their ID, title and year.
        :return: a list of movie objects
        """

        movieTuples = self.db.query("""
               SELECT id, name, publishedDate FROM movies
               """)

        movies = []
        for movieTuple in movieTuples:
            movies.append(Movie(id=movieTuple[0],
                                name=movieTuple[1],
                                publishedDate=movieTuple[2]))

        return movies
