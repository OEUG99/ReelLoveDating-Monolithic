from PyDataOpsKit import AbstractRepository
from backend.src.models.Genre import Genre


class GenreRepository(AbstractRepository):
    """
    This class is responsible for handling all database operations related to the Genre model.
    """

    def createTable(self):
        """
        Creates the table in the database if it does not exist.
        :return:
        :rtype:
        """

        try:
            self.db.query("""
                CREATE TABLE IF NOT EXISTS genres (
                    genreName VARCHAR(255) PRIMARY KEY,
                    actedInGenre VARCHAR(255),
                    belongsToGenre VARCHAR(255),
                    hasDirectedGenre VARCHAR(255),
                    isFavoriteOf VARCHAR(255)
                    )
                """)
            print("Genre table created successfully")
        except Exception as e:
            print("Error while creating the 'genres' table:", e)

    def add(self, genre: Genre):
        """
        Adds a genre to the database
        :param genre:
        :type genre:
        :return:
        rtype:
        """
        addSQL = """
        INSERT INTO genres (genreName, actedInGenre, belongsToGenre, hasDirectedGenre, isFavoriteOf)
        VALUES (%s, %s, %s, %s, %s)
        """

        self.db.query(addSQL, (genre.genreName,
                               genre.actedInGenre,
                               genre.belongsToGenre,
                               genre.hasDirectedGenre,
                               genre.isFavoriteOf))

    def update(self, obj):
        """
        Updates a genre in the database, returns the updated Genre object
        :param obj:
        :type obj:
        :return:
        :rtype:
        """
        pass

    def delete(self, genre):
        """
        Deletes a genre from the database
        :param genre:
        :type genre:
        :return:
        :rtype:
        """
        deleteSQL = """
        DELETE FROM genres WHERE genreName = %s
        """
        self.db.query(deleteSQL, (genre.genreName,))

    def get(self, genreName):
        """
        Gets a genre from the database via its name
        :param genreName:
        :type genreName:
        :return:
        :rtype:
        """
        getSQL = """
        SELECT * FROM genres WHERE genreName = %s
        """

        genreTuple = self.db.query(getSQL, (genreName,))[0]

        if genreTuple:
            return Genre(genreName=genreTuple[0],
                         actedInGenre=genreTuple[1],
                         belongsToGenre=genreTuple[2],
                         hasDirectedGenre=genreTuple[3],
                         isFavoriteOf=genreTuple[4])
        else:
            return None

    def getAll(self):
        """
        Gets all genres from the database
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
