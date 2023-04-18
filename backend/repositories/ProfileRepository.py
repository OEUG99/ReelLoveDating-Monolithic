from PyDataOpsKit import AbstractRepository
from PyDataOpsKit.DatabaseManager import DatabaseManager


class ProfileRepository(AbstractRepository):

    def __init__(self):
        self.db = DatabaseManager()
        self.create_table()

    def create_table(self):
        try:
            self.db.query("""
                CREATE TABLE IF NOT EXISTS profiles (
                    id VARCHAR(255) PRIMARY KEY,
                    visibility BOOLEAN,
                    firstName VARCHAR(255),
                    lastName VARCHAR(255),
                    bio VARCHAR(255),
                    gender VARCHAR(255),
                    age INTEGER,
                    location VARCHAR(255),
                    sexuality VARCHAR(255),
                    interests VARCHAR(255),
                    favoriteMovies VARCHAR(255)
                )
            """)
            return
        except Exception as e:
            print("Error while creating the 'profiles' table:", e)

        print("Profile table created successfully")

    def add(self, profile):
        print(f"Adding profile for user {profile.userID} to the database")
        result = self.db.query("""
        INSERT INTO profiles (id, visibility, firstName, lastName, bio, gender, age, location, sexuality, interests, favoriteMovies)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (profile.userID, profile.visibility, profile.firstName, profile.lastName, profile.bio, profile.gender,
              profile.age, profile.location, profile.sexuality, profile.interests, profile.favoriteMovies))
        print(result)

    def update(self, profile):
        pass

    def delete(self, profile):
        pass

    def get(self, profile):
        pass

    def get_all(self):
        pass

    def get_by_userID(self, userID):
        print(userID)
        profile = self.db.query("""
            SELECT * FROM profiles WHERE id = %s LIMIT 1
        """, (userID,))

        return profile

    def get_random(self, numProfilesToFetch):
        output = self.db.query("""
            SELECT * FROM profiles ORDER BY RANDOM() LIMIT 5
            """)
        print(output)
        return output

    def __del__(self):
        self.db.close()
