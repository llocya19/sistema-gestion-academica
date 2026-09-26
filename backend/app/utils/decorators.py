from functools import wraps

from flask import jsonify

from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt_identity,
    get_jwt
)

from app.modules.auth.models import Usuario



def requiere_rol(rol_requerido):

    def decorador(func):

        @wraps(func)
        def wrapper(*args, **kwargs):


            # Verificar JWT
            verify_jwt_in_request()


            # Obtener ID del usuario
            usuario_id = get_jwt_identity()


            usuario = Usuario.query.get(
                int(usuario_id)
            )


            # Usuario eliminado
            if not usuario:

                return jsonify({

                    "mensaje":
                    "Usuario no encontrado"

                }),401



            # Usuario desactivado
            if not usuario.status:

                return jsonify({

                    "mensaje":
                    "Usuario desactivado"

                }),403



            # Verificar rol desde BD
            if usuario.rol.name != rol_requerido:

                return jsonify({

                    "mensaje":
                    "No tiene permisos para acceder"

                }),403



            return func(*args, **kwargs)


        return wrapper


    return decorador