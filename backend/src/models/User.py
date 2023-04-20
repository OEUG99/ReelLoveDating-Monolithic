"""
Copyright by OEUG99
"""

import re
import uuid
from dataclasses import dataclass
import bcrypt
from PyDataOpsKit.AbstractModel import AbstractModel


@dataclass
class User(AbstractModel):
    """
    This user class models the user entity in the database.
    Whenever we get a users info from the database, we will create a user object.
    Whenever we want to create a new user, we will create a user object, and then add it to the database
    via the UserRepository.
    """
    id = None
    email = None
    raw_password = None

    def __init__(self, email, password, userID=None):
        """
        Creates a new user object.
        :param email:
        :type email:
        :param password:
        :type password:
        :param userID:
        :type userID:
        """

        if userID is not None:
            # if an id is provided, we can assume the password is hashed.
            # This is used when we are getting a user from the database.
            self.id = userID
            self.email = email
            self.password = password
            return

        if not validateUsername(email):
            raise ValueError("Username does not meet the minimum requirements.")

        if validatePassword(password):
            raise ValueError("Password does not meet the minium requirements. Passwords Must have at least 8 "
                             "characters, one uppercase letter, one lowercase letter, one number, and one special "
                             "character. It also can not be longer then 100 characters.")

        self.id = str(uuid.uuid4())
        self.email = email
        self.password = hashPassword(password)

    def toDict(self) -> dict:
        """
        Converts the user object to a dictionary.
        :return:
        :rtype:
        """
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password
        }

    def __repr__(self):
        """
        Returns a string representation of the user object.
        :return:
        :rtype:
        """
        return '<User %r>' % self.email


# Utility functions for the User class below:
def validateUsername(username) -> bool:
    """
    Validates the username meets the minimum requirements.
    :param username:
    :type username:
    :return:
    :rtype:
    """
    # default return value for now since no requirements are set.
    return True


def validatePassword(raw_password) -> bool:
    """
    Validates the password meets the minimum requirements.
    :param raw_password:
    :type raw_password:
    :return:
    :rtype:
    """
    print(len(raw_password))

    # Password must be at least 8 characters long
    if len(raw_password) >= 8:
        return False

    # Password not be longer then 50 characters
    if len(raw_password) > 50:
        return False

    # Password must contain at least one uppercase letter and one lowercase letter and one number
    # and one special character
    password_pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    return password_pattern.match(raw_password) is not None


def hashPassword(raw_password) -> str:
    """
    Hashes the password with bcrypt.
    :param raw_password:
    :type raw_password:
    :return:
    :rtype:
    """

    password_hash = bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt())
    return password_hash.decode()  # returning hash with salt.
