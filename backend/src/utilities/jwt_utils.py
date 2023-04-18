import datetime
import json
import os
import jwt


def getSecretKey():
    secret_key = os.environ.get("JWT_SECRET_KEY") or None

    if not secret_key:
        raise ValueError("JWT_SECRET_KEY not set in environment variables.")

    return secret_key


def generateToken(user):
    """Generates a JWT Token used for client authorization.
    :param user:
    :type user:
    :return: encoded JWT token
    :rtype:
    """
    # Getting values ready to be embedded in the JWT token
    userID = user.id
    expiration_date = datetime.datetime.today() + datetime.timedelta(days=1)  # 1 day expiration

    token = jwt.encode({'user_id': userID,
                        'exp': expiration_date},
                       getSecretKey(),
                       algorithm="HS256")

    return token


def decodeToken(encodedToken):
    """Decodes a JWT Token used for client authorization.
    :param encodedToken:
    :type encodedToken:
    :return: decoded JWT token
    :rtype:
    """

    try:
        decodedToken = jwt.decode(encodedToken, getSecretKey(), algorithms=["HS256"])
        return json.dumps(decodedToken)

    except jwt.ExpiredSignatureError:
        return "Token expired."

    except jwt.InvalidTokenError:
        return "Invalid token."