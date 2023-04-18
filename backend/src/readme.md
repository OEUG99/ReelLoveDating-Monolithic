# Backend


## What is this?
This is the backend server. It can only be accessed via HTTP requests to the gateways defined in
`api/`.

Everything in the directory `api/` is a flask blueprint. Each blueprint must be declared in the main flask
file, which is `app.py`. eg: `app.register_blueprint(authRoutes.bp)`

This is how you can make new gateway types. 

In these gateways, we use model classes in `models/` to store data. These models are the servers local 
representation of a certain entity. We employ the `repositories/` to save that local representation to
the database, and also `repositories/` can populate `models/` for us. For instance, lets say we need to get
a users profile, rather than getting back a json string from the database, the repository uses the model 
for profiles and inserts the data nicely into that, so we have a clean interface to work with. 

Models and repositories are using base classes, which are written as part of another library. You can find that repo by 
[clicking here](https://github.com/OEUG99/PyDataOpsKit). 

All this library does is sort of create a template for all the models and repos, as when you inherit and abstract
class in python, you are forced to have the same abstract method in the child class. 

Why do we do this? Well, this helps keeps things easy to understand by forcing us to stick to certain predetermined methods.
for instance, take the following example. 

I may write `ProfileRepository.getByID(id=10)` whereas when you guys are writing your own entities you may write
something like `ActorRepository.Get(id=4)`. Both technically do the same job, but by having an abstract base class
we can force ourselves to use predetermined methods, thus making our code more easier to understand across each other.


### Understanding JWT tokens.
Understanding JWT tokens is probably very important, as they are how we do user auth. For example, if we do not
have user authing, anyone could make a request to an http gateway, and sometimes we do want that. Take for instance
a bad actor making a request to change a users passwords. By requiring the user to have an auth token before changing password
we can prevent bad actors.

`utilities/jwt_utils.py` has prewritten functions for decoding JWT tokens. This is probably the only function you will
need out of that helper file. 

For a good example of how the JWT token gets transfered from the CLIENT back to the server can be seen with the
`validate` gateway inside of `api/authRoutes`. 

```python
@bp.route('/validate', methods=['POST'])
def validate() -> Response:
    """ The validate endpoint is used to validate a JWT token.
    :return: HTTP Response
    :rtype: Response
    """
    data = request.get_json()
    token = data.get('token') # LOOK HERE ~ this is how we get it from the client.

    # validating the token exists
    if not token:
        return Response(status=400)

    # Decoding and validating the token
    try:
        decodedToken = decodeToken(token)
        return Response(response=decodedToken, status=200)

    except Exception as e:
        return Response(response=str(e), status=400)
```

### Tools you may need for debugging.
Postman is a commonly used HTTP client; however, if you are using PyCharm (not community edition) you have HTTP requests
built in to your IDE. 
`backend/misc/http-tests` has examples of http tests for PyCharm. 

There is also [PAW/RapidAPI](https://paw.cloud/) I used this one quite a lot before discovering PyCharm's 
