from PyDataOpsKit import AbstractRepository
from backend.src.models.Like import Like
from typing import List


class LikeRepository(AbstractRepository):
    """
   This class is responsible for handling all database operations related to the Like model.
   """

    def createTable(self):
        """
       Creates the table in the database if it does not exist.
       """
        try:
            self.db.query("""
               CREATE TABLE IF NOT EXISTS likes (
                   id VARCHAR(255) PRIMARY KEY,
                   userID VARCHAR(255),
                   secondaryUserID VARCHAR(255)
                   )
               """)
            print("Like table created successfully")
        except Exception as e:
            print("Error while creating the 'likes' table:", e)

    def add(self, like):
        """
       Adds a like to the database
       """
        self.db.query("""
       INSERT INTO likes (id, userID, secondaryUserID)
       VALUES (%s, %s, %s)
       """, (like.id,
             like.userID,
             like.secondaryUserID))

    def update(self, like):
        """
           Updates a like in the database, returns the updated Like object
              :param like:
              :type like:
              :return:
              :rtype:
              """
        print(f"Updating like for user {like.userID} in the database")

        updateSQL = """
                 UPDATE likes
                 SET userID = %s,
                     secondaryUserID = %s,
                 WHERE id = %s
                 """

        self.db.query(updateSQL,
                      (like.userID,
                       like.secondaryUserID,
                       like.id))
        pass

    def delete(self, like):
        """
       Deletes a like from the database
       """
        deleteSQL = """
       DELETE FROM likes WHERE id = %s
       """
        self.db.query(deleteSQL, (like.id,))

    def get(self, likeID):
        """
        Gets a like from the database via its ID
        """
        query = """
            SELECT id, userID, secondaryUserID
            FROM likes
            WHERE id = %s
        """
        result = self.db.query(query, (likeID,))
        row = result.fetchone()
        if row:
            like = Like(id=row[0], userID=row[1], secondaryUserID=row[2])
            return like
        else:
            return None

    def getCount(self):
        pass

    def getAll(self):
        """
        Gets all likes in the database
        """
        query = """
                   SELECT id, userID, secondaryUserID
                   FROM likes
               """
        result = self.db.query(query)
        likes = []
        for row in result:
            like = Like(id=row[0], userID=row[1], secondaryUserID=row[2])
            likes.append(like)
        return likes

    def getAllByUserID(self, userID):
        query = """
                      SELECT id
                        FROM likes
                        WHERE secondaryUserID = %s
            """

        result = self.db.query(query, (userID,))
        likes = []
        for row in result:
            like = row[0]
            likes.append(like)

        return likes

    def getByAttribute(self, attribute):
        pass

    def getList(self, limit, offset=None):
        pass
