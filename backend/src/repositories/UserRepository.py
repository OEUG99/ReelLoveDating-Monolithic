from PyDataOpsKit.AbstractRepoistory import AbstractRepository
from backend.src.models.User import User


class UserRepository(AbstractRepository):

    def createTable(self):
        """
        creates the users table in the database if it does not yet exists.
        :return:
        :rtype:
        """
        try:
            self.db.query("""
                CREATE TABLE IF NOT EXISTS users (
                    id VARCHAR(255) PRIMARY KEY,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL
                )
            """)
        except Exception as e:
            print("Error while creating the 'users' table:", e)

    def add(self, user):
        self.db.query("""
                    INSERT INTO users (id, email, password)
                    VALUES (%s, %s, %s)
                    ON DUPLICATE KEY UPDATE email = %s
                """, (user.id, user.email, user.password, user.email))

    def update(self, user):
        pass

    def delete(self, user):
        pass

    def get(self, id):
        pass

    def getAll(self):
        pass

    def getByUsername(self, email: str):
        """
        searches the database for a user with the given email and returns a User object if found.
        if no user is found, returns None

        :param email:
        :return:User() or None
        :rtype:
        """
        userTuple = self.db.query("""
            SELECT * FROM users WHERE email = %s LIMIT 1
        """, (email,))[0]

        if userTuple:
            return User(userID=userTuple[0],
                        email=userTuple[1],
                        password=userTuple[2])
        else:
            return None

    def checkPassword(self, email: str, password: str):
        """
        checks if the given password hash matches the password of the user with the given email.
        :param email: str
        :type email: str
        :param password: str
        :type password: str
        :return:
        :rtype:
        """

        result = self.db.query("""
            SELECT * FROM users WHERE email = ? AND password = ? LIMIT 1
        """, (email, password))

        return result

    def getList(self, limit, offset=None):
        pass

    def getCount(self):
        pass

    def getByAttribute(self, attribute):
        pass

    def __del__(self):
        self.db.close()