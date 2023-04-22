from PyDataOpsKit import AbstractRepository
from backend.src.models import Actor


class ActorRepository(AbstractRepository):

    def createTable(self):
        self.db.query("""
            CREATE TABLE IF NOT EXISTS actors (
                id VARCHAR(255) PRIMARY KEY,
                firstName VARCHAR(255),
                lastName VARCHAR(255),
                age INTEGER
            )
        """)


    def add(self, actor):
        self.db.query("""
            INSERT INTO actors (id, firstName, lastName, age)
            VALUES (%s, %s, %s, %s)
        """, (actor.id, actor.firstName, actor.lastName, actor.age))


    def update(self, actor):
        self.db.query("""
            UPDATE actors
            SET firstName = %s,
                lastName = %s,
                age = %s
            WHERE id = %s
        """, (actor.firstName, actor.lastName, actor.age, actor.id))

    def delete(self, obj):
        pass

    def get(self, id):
        query = self.db.query("""
            SELECT * FROM actors WHERE id = %s LIMIT 1
        """, (id,))[0]
        if query:
            return Actor(id=query[0], firstName=query[1], lastName=query[2], age=query[3])
        else:
            return None


    def getAll(self):
        pass

    def getList(self, limit, offset=None):
        pass

    def getCount(self):
        pass

    def getByAttribute(self, attribute):
        pass

    def getByFirstNameAndLastName(self, leadActorFirstName, leadActorLastName):
        query = self.db.query("""
            SELECT * FROM actors WHERE firstName = %s AND lastName = %s LIMIT 1
        """, (leadActorFirstName, leadActorLastName))

        query = query[0] if query else None

        if query:
            return Actor(id=query[0], firstName=query[1], lastName=query[2], age=query[3])