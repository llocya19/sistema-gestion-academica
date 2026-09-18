from flask import Flask 
 
from app.config.settings import Config 
 
from app.extensions.database import db 
from app.extensions.jwt import jwt 
from app.extensions.cors import cors 
from app.extensions.migrate import migrate 


# Importar modelos
from app.modules.auth import models as auth_models
from app.modules.academic import models as academic_models
from app.modules.analytics import models as analytics_models
from app.modules.admin.routes import admin_bp


# Importar rutas
from app.modules.auth.routes import auth_bp



def create_app(): 
 
    app = Flask(__name__) 
 
    app.config.from_object(Config) 
 
 
    # Inicializar extensiones
 
    db.init_app(app) 
 
    jwt.init_app(app) 
 
    cors.init_app(app) 
     
    migrate.init_app(app, db)



    # Registrar rutas

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)


    @app.route("/") 
    def home(): 
 
        return { 
            "message": "API Sistema Gestión Académica funcionando", 
            "status": "success" 
        } 
 
 
    return app