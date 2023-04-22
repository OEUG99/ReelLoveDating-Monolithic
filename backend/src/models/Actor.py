import uuid
from dataclasses import dataclass

from PyDataOpsKit import AbstractModel


@dataclass
class Actor(AbstractModel):
    def __init__(self, id=None, firstName=None, lastName=None, age=None):
        self.id = id or str(uuid.uuid4())
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "age": self.age
        }
