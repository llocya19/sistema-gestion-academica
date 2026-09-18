from flask import Blueprint, request, jsonify

from flask_jwt_extended import create_access_token

from app.modules.auth.services import autenticar_usuario


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)



@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():


    data = request.get_json()


    usuario = autenticar_usuario(
        data.get("email"),
        data.get("password")
    )


    if not usuario:

        return jsonify({
            "mensaje":"Credenciales incorrectas"
        }),401



    token = create_access_token(

        identity=str(usuario.id),

        additional_claims={

            "rol": usuario.rol.name,

            "email": usuario.email

        }

    )



    return jsonify({

        "mensaje":"Login correcto",

        "access_token":token,

        "usuario":{

            "id":usuario.id,

            "email":usuario.email,

            "persona":{

                "nombres":usuario.persona.nombres,

                "apellidos":usuario.persona.apellidos

            },

            "rol":usuario.rol.name

        }

    })


#ddedede
from flask_jwt_extended import jwt_required

from app.utils.decorators import requiere_rol



@auth_bp.route(
    "/admin-test",
    methods=["GET"]
)
@requiere_rol("ADMINISTRADOR")
def admin_test():

    return jsonify({

        "mensaje":
        "Bienvenido administrador"

    })