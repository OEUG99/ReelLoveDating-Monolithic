from PyDataOpsKit.AbstractRepoistory import AbstractRepository
from PyDataOpsKit.DatabaseManager import DatabaseManager

from backend.models import User


class UserRepository(AbstractRepository):

    def __init__(self):
        self.db = DatabaseManager()
        self.create_table()

    def create_table(self):
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

    def get_all(self):
        pass

    def get_by_username(self, email):
        """
        searches the database for a user with the given username and returns a User object if found.
        if no user is found, returns None

        :param username:
        :type username:
        :return:User() or None
        :rtype:
        """
        userTuple = self.db.query("""
            SELECT * FROM users WHERE email = %s LIMIT 1
        """, (email,))

        if userTuple:
            return User(userID=userTuple[0],
                        username=userTuple[1],
                        password=userTuple[2])
        else:
            return None

    def check_password(self, email, password):

        result = self.db.query("""
            SELECT * FROM users WHERE email = ? AND password = ? LIMIT 1
        """, (email, password))

        return result

    def __del__(self):
        self.db.close()