from PyDataOpsKit import AbstractRepository
from backend.src.models.Match import Match




class MatchRepository(AbstractRepository):
   """
  This class is responsible for handling all database operations related to the Match model.
  """


   def createTable(self):
       """
      Creates the table in the database if it does not exist.
      """
       try:
           self.db.query("""
              CREATE TABLE IF NOT EXISTS matches (
                  id VARCHAR(255) PRIMARY KEY,
                  userID VARCHAR(255),
                  secondaryUserID VARCHAR(255)
                  )
              """)
           print("Match table created successfully")
       except Exception as e:
           print("Error while creating the 'matches' table:", e)


   def add(self, match):
       """
      Adds a match to the database
      """
       self.db.query("""
      INSERT INTO matches (id, userID, secondaryUserID)
      VALUES (%s, %s, %s)
      """, (match.id,
            match.userID,
            match.secondaryUserID))


   def update(self, match):
       pass


   def delete(self, match):
       """
      Deletes a match from the database
      """
       deleteSQL = """
      DELETE FROM matches WHERE id = %s
      """
       self.db.query(deleteSQL, (match.id,))


   def get(self, matchID):
       """
       Gets a match from the database via its ID
       """
       pass


   def getCount(self):
       pass


   def getAll(self):
       """
       Gets all matches in the database
       """
       query = """
                  SELECT id, userID, secondaryUserID
                  FROM matches
              """
       result = self.db.query(query)
       matches = []
       for row in result:
           match = Match(id=row[0], userID=row[1], secondaryUserID=row[2])
           matches.append(match)
       return matches


   def getByAttribute(self, attribute):
       pass


   def getList(self, limit, offset=None):
       pass
