from flask import Flask

from app.config.settings import Config

from app.extensions.database import db
from app.extensions.jwt import jwt
from app.extensions.cors import cors


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # Inicializar extensiones

    db.init_app(app)

    jwt.init_app(app)

    cors.init_app(app)


    @app.route("/")
    def home():

        return {
            "message": "API Sistema Gestión Académica funcionando",
            "status": "success"
        }


    return app