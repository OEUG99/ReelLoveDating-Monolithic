import uuid
from dataclasses import dataclass
from PyDataOpsKit import AbstractModel


@dataclass
class Match(AbstractModel):
    """
  This Match class models the match entity in the database.
  Whenever we want to create a new match, we will create a match object, and then add it to the database
  via the MatchRepository.
  """

    def __init__(self, userID: str = None, secondaryUserID: str = None, id: str = None):
        """
      creates a new match object
      :param id:
      :type id:
      :param userID:
      :type userID:
      :param secondaryUserID:
      :type secondaryUserID:
      """

        if id is None:
            id = str(uuid.uuid4())

        self.id = id
        self.userID = userID
        self.secondaryUserID = secondaryUserID

    def toDict(self) -> dict:
        """
      Converts the match object to a dictionary.
      :return:
      :rtype:
      """
        return {
            "id": self.id,
            "userID": self.userID,
            "secondaryUserID": self.secondaryUserID
        }

    def __repr__(self):
        return self.id
