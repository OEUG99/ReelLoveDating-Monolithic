from PyDataOpsKit import AbstractRepository
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
                    favoriteMovies VARCHAR(255)
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
        print(f"Adding profile for user {profile.userID} to the database")
        self.db.query("""
        INSERT INTO profiles (id, visibility, firstName, lastName, bio, gender, age, location, sexuality, interests, favoriteMovies)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (profile.userID, profile.visibility, profile.firstName, profile.lastName, profile.bio, profile.gender,
              profile.age, profile.location, profile.sexuality, profile.interests, profile.favoriteMovies))

    def update(self, profile):
        """
        Updates a profile in the database, returns the updated Profile object
        :param profile:
        :type profile:
        :return:
        :rtype:
        """
        print(f"Updating profile for user {profile.userID} in the database")

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
               favoriteMovies = %s
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
                       profile.userID))

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
        """, (userID,))[0]

        print(query)

        if query:
            return Profile(userID=query[0],
                           visibility=query[1],
                           firstName=query[2],
                           lastName=query[3],
                           bio=query[4])
        else:
            return None

    def getRandom(self, numProfilesToFetch):
        """
        Fetches n-number of random number of profiles from the database.
        :return:
        :rtype:
        """

        query = self.db.query("""
            SELECT * FROM profiles ORDER BY RANDOM() LIMIT 5
            """)

        if query is None:
            return None

        profiles = []
        for profilesTuples in query:
            profiles.append(Profile(userID=profilesTuples[0],
                                    visibility=profilesTuples[1],
                                    firstName=profilesTuples[2],
                                    lastName=profilesTuples[3],
                                    bio=profilesTuples[4],
                                    gender=profilesTuples[5],
                                    age=profilesTuples[6],
                                    location=profilesTuples[7],
                                    sexuality=profilesTuples[8],
                                    interests=profilesTuples[9],
                                    favoriteMovies=profilesTuples[10]))

        return profiles

    def getList(self, limit, offset=None):
        pass

    def getCount(self):
        pass

    def getByAttribute(self, attribute):
        pass

    def __del__(self):
        self.db.close()
