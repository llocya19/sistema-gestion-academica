from functools import wraps

from flask import jsonify

from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt
)



def requiere_rol(rol_requerido):

    def decorador(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            verify_jwt_in_request()

            claims = get_jwt()

            rol_usuario = claims.get(
                "rol"
            )


            if rol_usuario != rol_requerido:

                return jsonify({

                    "mensaje":
                    "No tiene permisos para acceder"

                }),403


            return func(*args, **kwargs)


        return wrapper

    return decorador