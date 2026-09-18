from werkzeug.security import check_password_hash

from app.modules.auth.models import Usuario


def autenticar_usuario(email, password):

    usuario = Usuario.query.filter_by(
        email=email
    ).first()


    if not usuario:
        return None


    if not check_password_hash(
        usuario.password_hash,
        password
    ):
        return None


    return usuario