from flask import Flask

from app.config.settings import Config

from app.extensions.database import db
from app.extensions.jwt import jwt
from app.extensions.cors import cors
from app.extensions.migrate import migrate

from app.modules.auth import models

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # Inicializar extensiones

    db.init_app(app)

    jwt.init_app(app)

    cors.init_app(app)
    
    migrate.init_app(app, db)


    @app.route("/")
    def home():

        return {
            "message": "API Sistema Gestión Académica funcionando",
            "status": "success"
        }


    return app