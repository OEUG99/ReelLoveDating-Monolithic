from PyDataOpsKit import AbstractModel


class Actor(AbstractModel):
    def __init__(self, id, firstName, lastName, age):
        self.id = id
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
