from werkzeug.security import check_password_hash
from app.modules.auth.models import Usuario


def autenticar_usuario(email, password):

    usuario = Usuario.query.filter_by(
        email=email
    ).first()


    if not usuario:
        raise ValueError("Usuario no encontrado")


    if not check_password_hash(
        usuario.password_hash,
        password
    ):
        raise ValueError("Contraseña incorrecta")


    if usuario.status != "ACTIVO":
        raise ValueError("Usuario desactivado")


    return usuario