from PyDataOpsKit import AbstractRepository

from backend.src.models import Director
from backend.src.models.Profile import Profile


class ProfileRepository(AbstractRepository):

    def createTable(self):
        """
        Creates the profiles table in the database if it does not exist.
        :return:
        :rtype:
        """
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
                    favoriteMovies VARCHAR(255),
                    favoriteActor VARCHAR(255),
                    favoriteDirector VARCHAR(255)
                )
            """)
            print("Profile table created successfully")
        except Exception as e:
            print("Error while creating the 'profiles' table:", e)

    def add(self, profile):
        """
        Adds a profile to the database
        :param profile:
        :type profile:
        :return:
        :rtype:
        """
        print(f"Adding profile for user {profile.id} to the database")
        self.db.query("""
        INSERT INTO profiles (id, visibility, firstName, lastName, bio, gender, age, location, sexuality, interests, favoriteMovies, favoriteActor, favoriteDirector)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            visibility = VALUES(visibility),
            firstName = VALUES(firstName),
            lastName = VALUES(lastName),
            bio = VALUES(bio),
            gender = VALUES(gender),
            age = VALUES(age),
            location = VALUES(location),
            sexuality = VALUES(sexuality),
            interests = VALUES(interests),
            favoriteMovies = VALUES(favoriteMovies),
            favoriteActor = VALUES(favoriteActor),
            favoriteDirector = VALUES(favoriteDirector)
        """, (profile.id, profile.visibility, profile.firstName, profile.lastName, profile.bio, profile.gender,
              profile.age, profile.location, profile.sexuality, profile.interests, profile.favoriteMovies,
              profile.favoriteActor, profile.favoriteDirector))

    def update(self, profile):
        """
        Updates a profile in the database, returns the updated Profile object
        :param profile:
        :type profile:
        :return:
        :rtype:
        """
        print(f"Updating profile for user {profile.id} in the database")

        updateSQL = """
           UPDATE profiles
           SET visibility = %s, 
               firstName = %s,
               lastName = %s,
               bio = %s,
               gender = %s,
               age = %s,
               location = %s,
               sexuality = %s,
               interests = %s,
               favoriteMovies = %s,
               favoriteActor = %s,
               favoriteDirector = %s
           WHERE id = %s
           """

        self.db.query(updateSQL,
                      (profile.visibility,
                       profile.firstName,
                       profile.lastName,
                       profile.bio,
                       profile.gender,
                       profile.age,
                       profile.location,
                       profile.sexuality,
                       profile.interests,
                       profile.favoriteMovies,
                       profile.favoriteActor,
                       profile.favoriteDirector,
                       profile.id))

    def delete(self, profile):
        pass

    def get(self, profile):
        pass

    def getAll(self):
        pass

    def getByUserID(self, userID):
        """
        searches the database for a profile with the given userID and returns a Profile object if found.
        :param userID:
        :type userID:
        :return:
        :rtype:
        """
        query = self.db.query("""
            SELECT * FROM profiles WHERE id = %s LIMIT 1;
        """, (userID,))

        query = query[0] if query else None

        print(query)

        if query:
            return Profile(userID=query[0],
                           visibility=query[1],
                           firstName=query[2],
                           lastName=query[3],
                           bio=query[4],
                           gender=query[5],
                           age=query[6],
                           location=query[7],
                           sexuality=query[8],
                           interests=query[9],
                           favoriteMovies=query[10],
                           favoriteActor=query[11],
                           favoriteDirector=query[12])
        else:
            return None

    def getRandom(self):
        """
        Fetches n-number of random number of profiles from the database.
        :return:
        :rtype:
        """

        query = self.db.query("""
            SELECT id FROM profiles ORDER BY RAND() LIMIT 1;
            """)[0][0]

        return query

    def getMatchedRandom(self, userID):
        """
        matched with the getRandom function to get a random profile
        :return:
        :rtype:
        """

        query = self.db.query(f"""
            SELECT p2.id
            FROM profiles p1, profiles p2
            WHERE p1.id = {userID} AND (p1.favoriteMovies = p2.favoriteMovies OR
                                           p1.favoriteActor = p2.favoriteActor OR
                                           p1.favoriteDirector = p2.favoriteDirector)
            ORDER BY RAND() -- Randomize the result
            LIMIT 1; -- Limit to one row
            """)[0][0]

        return query

    def getList(self, limit, offset=None):
        pass

    def getCount(self):
        pass

    def getByAttribute(self, attribute):
        pass

    def __del__(self):
        self.db.close()
