from flask import Blueprint, jsonify, request

from flask_jwt_extended import jwt_required


from app.utils.decorators import requiere_rol


from app.modules.admin.services import (
    listar_usuarios,
    crear_usuario,
    actualizar_usuario,
    cambiar_estado_usuario,
    listar_roles,
    listar_permisos,
    asignar_permisos_rol,
    obtener_permisos_rol
)




admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/api/admin"
)



# ==========================================================
# PRUEBA MODULO ADMIN
# ==========================================================

@admin_bp.route(
    "/test",
    methods=["GET"]
)
@jwt_required()
@requiere_rol("ADMINISTRADOR")
def admin_test():


    return jsonify({

        "mensaje":
        "Modulo administrador funcionando"

    })




# ==========================================================
# LISTAR USUARIOS
# ==========================================================

@admin_bp.route(
    "/users",
    methods=["GET"]
)
@jwt_required()
@requiere_rol("ADMINISTRADOR")
def users():


    usuarios = listar_usuarios()


    return jsonify({

        "usuarios": usuarios

    })





# ==========================================================
# CREAR USUARIO
# ==========================================================

@admin_bp.route(
    "/users",
    methods=["POST"]
)
@jwt_required()
@requiere_rol("ADMINISTRADOR")
def create_user():


    try:


        data = request.get_json()


        usuario = crear_usuario(data)



        return jsonify({

            "mensaje":
            "Usuario creado correctamente",


            "usuario": {


                "id":
                usuario.id,


                "email":
                usuario.email,


                "estado":
                usuario.status,


                "rol": {

                    "id":
                    usuario.rol.id,


                    "nombre":
                    usuario.rol.name

                },


                "persona": {

                    "dni":
                    usuario.persona.dni,


                    "nombres":
                    usuario.persona.nombres,


                    "apellidos":
                    usuario.persona.apellidos

                }


            }


        }), 201



    except ValueError as error:


        return jsonify({

            "mensaje":
            str(error)

        }),400

# ==========================================================
# ACTUALIZAR USUARIO
# ==========================================================

@admin_bp.route(
    "/users/<int:id>",
    methods=["PUT"]
)
@jwt_required()
@requiere_rol("ADMINISTRADOR")
def update_user(id):


    try:

        data = request.get_json()


        usuario = actualizar_usuario(
            id,
            data
        )


        return jsonify({

            "mensaje":
            "Usuario actualizado correctamente",

            "usuario":{

                "id":usuario.id,

                "email":usuario.email,

                "rol":{

                    "id":usuario.rol.id,

                    "nombre":usuario.rol.name

                },

                "persona":{

                    "nombres":
                    usuario.persona.nombres,

                    "apellidos":
                    usuario.persona.apellidos

                }

            }

        })


    except ValueError as error:


        return jsonify({

            "mensaje":str(error)

        }),400

# ==========================================================
# CAMBIAR ESTADO USUARIO
# ==========================================================

@admin_bp.route(
    "/users/<int:id>/status",
    methods=["PATCH"]
)
@jwt_required()
@requiere_rol("ADMINISTRADOR")
def update_status(id):


    try:

        data = request.get_json()


        usuario = cambiar_estado_usuario(
            id,
            data["status"]
        )


        return jsonify({

            "mensaje":
            "Estado actualizado correctamente",


            "usuario":{

                "id":
                usuario.id,


                "email":
                usuario.email,


                "estado":
                usuario.status

            }


        })


    except ValueError as error:


        return jsonify({

            "mensaje":
            str(error)

        }),400

# ==========================================================
# LISTAR ROLES
# ==========================================================

@admin_bp.route(
    "/roles",
    methods=["GET"]
)
@jwt_required()
@requiere_rol("ADMINISTRADOR")
def roles():


    datos = listar_roles()


    return jsonify({

        "roles": datos

    })

# ==========================================================
# LISTAR PERMISOS
# ==========================================================

@admin_bp.route(
    "/permissions",
    methods=["GET"]
)
@jwt_required()
@requiere_rol("ADMINISTRADOR")
def permissions():


    datos = listar_permisos()


    return jsonify({

        "permisos": datos

    })

# ==========================================================
# ASIGNAR PERMISOS A ROL
# ==========================================================

@admin_bp.route(
    "/roles/<int:id>/permissions",
    methods=["POST"]
)
@jwt_required()
@requiere_rol("ADMINISTRADOR")
def assign_permissions(id):


    try:

        data = request.get_json()


        rol = asignar_permisos_rol(
            id,
            data["permissions"]
        )


        return jsonify({

            "mensaje":
            "Permisos asignados correctamente",


            "rol":{

                "id":
                rol.id,

                "nombre":
                rol.name

            }

        })


    except ValueError as error:


        return jsonify({

            "mensaje":
            str(error)

        }),400
@admin_bp.route(
    "/roles/<int:id>/permissions",
    methods=["GET"]
)
@jwt_required()
@requiere_rol("ADMINISTRADOR")
def get_role_permissions(id):


    try:

        resultado = obtener_permisos_rol(id)


        return jsonify({

            "rol":{

                "id":resultado["id"],

                "nombre":resultado["nombre"]

            },

            "permisos":
            resultado["permisos"]

        })


    except ValueError as error:


        return jsonify({

            "mensaje":str(error)

        }),400