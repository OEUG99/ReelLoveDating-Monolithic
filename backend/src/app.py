from flask import Flask

from backend.src.api import authRoutes, profileRoutes, likeRoutes, actorRoutes, directorRoutes, movieRoutes

app = Flask(__name__)

# Registering the blueprints
app.register_blueprint(authRoutes.bp)
app.register_blueprint(profileRoutes.bp)
app.register_blueprint(likeRoutes.bp)
app.register_blueprint(actorRoutes.bp)
app.register_blueprint(directorRoutes.bp)
app.register_blueprint(movieRoutes.bp)

@app.route('/')
def healthCheck():
    return 'HEALTHY'

if __name__ == '__main__':
    app.run()
