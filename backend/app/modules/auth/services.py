from datetime import datetime
from werkzeug.security import check_password_hash

from app.extensions.database import db
from app.modules.auth.models import Usuario



def autenticar_usuario(email, password):


    if not email or not password:
        raise ValueError(
            "Correo y contraseña son obligatorios"
        )


    email = email.lower().strip()


    usuario = Usuario.query.filter_by(
        email=email
    ).first()


    if not usuario:
        raise ValueError(
            "Credenciales incorrectas"
        )


    if not check_password_hash(
        usuario.password_hash,
        password
    ):
        raise ValueError(
            "Credenciales incorrectas"
        )


    if not usuario.status:
        raise ValueError(
            "Usuario desactivado"
        )


    usuario.last_login = datetime.utcnow()

    db.session.commit()


    return usuario