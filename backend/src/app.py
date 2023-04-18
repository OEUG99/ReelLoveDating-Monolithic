from flask import Flask

from backend.src.api import authRoutes, profileRoutes

app = Flask(__name__)

# Registering the blueprints
app.register_blueprint(authRoutes.bp)
app.register_blueprint(profileRoutes.bp)


@app.route('/')
def healthCheck():
    return 'HEALTHY'


if __name__ == '__main__':
    app.run()
