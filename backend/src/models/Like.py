import uuid
from dataclasses import dataclass
from PyDataOpsKit import AbstractModel


@dataclass
class Like(AbstractModel):
    """
   This Like class models the like entity in the database.
   Whenever we want to create a new like, we will create a like object, and then add it to the database
   via the LikeRepository.
   """

    def __init__(self, userID: str = None, secondaryUserID: str = None, id: str = None):
        """
       creates a new like object
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
       Converts the like object to a dictionary.
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
