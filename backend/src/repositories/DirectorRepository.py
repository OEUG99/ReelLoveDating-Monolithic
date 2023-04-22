from PyDataOpsKit import AbstractRepository
from backend.src.models.Director import Director


class DirectorRepository(AbstractRepository):
    """
    This class is responsible for handling all database operations related to the Director model.
    """

    def createTable(self):
        """
        Creates the table in the database if it does not exist.
        :return:
        :rtype:
        """
        try:
            self.db.query("""
                CREATE TABLE IF NOT EXISTS directors (
                    id VARCHAR(255) PRIMARY KEY,
                    firstName VARCHAR(255),
                    lastName VARCHAR(255),
                    directedMovie VARCHAR(255),
                    directedInGenre VARCHAR(255),
                    isFavoriteOf VARCHAR(255)
                    )
                """)
            print("Director table created successfully.")
        except Exception as e:
            print("Error while creating the 'directors' table:", e)

    def add(self, director: Director):
        """
        Adds a movie to the database
        :param director:
        :type director:
        :return:
        :rtype:
        """
        addSQL = """
        INSERT INTO directors (id, firstName, lastName, directedMovie, directedInGenre, isFavoriteOf)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        print(director.id, "HERE")

        self.db.query(addSQL, (director.id,
                               director.firstName,
                               director.lastName,
                               director.directedMovie,
                               director.directedInGenre,
                               director.isFavoriteOf))

    def update(self, obj):
        """
        Updates a director in the database, returns the updated Director object
        :param obj:
        :type obj:
        :return:
        :rtype:
        """
        pass

    def delete(self, director):
        """
        Deletes a director from the database
        :param director:
        :type director:
        :return:
        :rtype:
        """
        deleteSQL = """
        DELETE FROM directors WHERE directorID = %s
        """
        self.db.query(deleteSQL, (director.directorID,))

    def get(self, directorID):
        """
        Gets a director from the database via its ID
        :param directorID:
        :type directorID:
        :return:
        :rtype:
        """
        getSQL = """
        SELECT * FROM directors WHERE id = %s
        """

        directorTuple = self.db.query(getSQL, (directorID,))[0]

        if directorTuple:
            return Director(directorID=directorTuple[0],
                            firstName=directorTuple[1],
                            lastName=directorTuple[2],
                            directedMovie=directorTuple[3],
                            directedInGenre=directorTuple[4],
                            isFavoriteOf=directorTuple[5])
        else:
            return None

    def getAll(self):
        """
        Gets all directors from the database
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

    def getByFirstNameAndLastName(self, directorFirstName, directorLastName):
        """
        Gets a director from the database via its first and last name
        :param directorFirstName:
        :type directorFirstName:
        :param directorLastName:
        :type directorLastName:
        :return:
        :rtype:
        """

        directorTuple = self.db.query("""
        SELECT * FROM directors WHERE firstName = %s AND lastName = %s
        """, (directorFirstName, directorLastName))

        directorTuple = directorTuple[0] if directorTuple else None

        if directorTuple:
            return Director(directorID=directorTuple[0],
                            firstName=directorTuple[1],
                            lastName=directorTuple[2],
                            directedMovie=directorTuple[3],
                            directedInGenre=directorTuple[4],
                            isFavoriteOf=directorTuple[5])
