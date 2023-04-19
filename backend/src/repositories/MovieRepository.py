from PyDataOpsKit import AbstractRepository


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
        pass

    def add(self, obj):
        """
        Adds a movie to the database
        :param obj:
        :type obj:
        :return:
        :rtype:
        """
        pass

    def update(self, obj):
        """
        Updates a movie in the database, returns the updated Movie object
        :param obj:
        :type obj:
        :return:
        :rtype:
        """
        pass

    def delete(self, obj):
        """
        Deletes a movie from the database
        :param obj:
        :type obj:
        :return:
        :rtype:
        """
        pass

    def get(self, movieID):
        """
        Gets a movie from the database via its ID
        :param movieID:
        :type movieID:
        :return:
        :rtype:
        """
        pass

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

