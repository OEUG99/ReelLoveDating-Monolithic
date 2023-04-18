from flask import Flask

from backend.api import profile, auth

app = Flask(__name__)

# Registering the blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(profile.bp)


@app.route('/')
def healthCheck():
    return 'HEALTHY'


if __name__ == '__main__':
    app.run()
