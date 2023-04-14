from flask import Flask

from api import user_routes

app = Flask(__name__)

# Registering the blueprints
app.register_blueprint(user_routes.bp)


@app.route('/')
def healthCheck():
    return 'HEALTHY'


if __name__ == '__main__':
    app.run()
