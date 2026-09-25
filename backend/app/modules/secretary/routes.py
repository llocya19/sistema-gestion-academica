from flask import Blueprint, jsonify, request

from flask_jwt_extended import jwt_required

from app.utils.decorators import requiere_rol

from app.modules.secretary.services import (

    listar_estudiantes,

    crear_estudiante,

    actualizar_estudiante,

    cambiar_estado_estudiante,

    importar_estudiantes_excel,

    listar_docentes,
    crear_docente,
    actualizar_docente,
    cambiar_estado_docente,
    importar_docentes_excel

)
secretary_bp = Blueprint(
    "secretary",
    __name__,
    url_prefix="/api/secretary"
)


@secretary_bp.route(
    "/test",
    methods=["GET"]
)
def secretary_test():

    return jsonify({

        "mensaje":
        "Modulo secretaria funcionando"

    })

# ==========================================================
# LISTAR ESTUDIANTES
# ==========================================================

@secretary_bp.route(
    "/students",
    methods=["GET"]
)
@jwt_required()
@requiere_rol("SECRETARIA")
def students():


    datos = listar_estudiantes()


    return jsonify({

        "estudiantes": datos

    })

# ==========================================================
# CREAR ESTUDIANTE
# ==========================================================

@secretary_bp.route(
    "/students",
    methods=["POST"]
)
@jwt_required()
@requiere_rol("SECRETARIA")
def create_student():


    try:

        data = request.get_json()


        estudiante = crear_estudiante(data)


        return jsonify({

            "mensaje":
            "Estudiante creado correctamente",


            "estudiante": {

                "id":
                estudiante.id,


                "codigo":
                estudiante.student_code,


                "persona": {

                    "dni":
                    estudiante.persona.dni,


                    "nombres":
                    estudiante.persona.nombres,


                    "apellidos":
                    estudiante.persona.apellidos

                }

            }

        }),201


    except ValueError as error:


        return jsonify({

            "mensaje":
            str(error)

        }),400

# ==========================================================
# ACTUALIZAR ESTUDIANTE
# ==========================================================

@secretary_bp.route(
    "/students/<int:id>",
    methods=["PUT"]
)
@jwt_required()
@requiere_rol("SECRETARIA")
def update_student(id):


    try:

        data = request.get_json()


        estudiante = actualizar_estudiante(
            id,
            data
        )


        return jsonify({

            "mensaje":
            "Estudiante actualizado correctamente",


            "estudiante": {

                "id":
                estudiante.id,


                "codigo":
                estudiante.student_code,


                "persona": {

                    "nombres":
                    estudiante.persona.nombres,


                    "apellidos":
                    estudiante.persona.apellidos

                }

            }

        })


    except ValueError as error:


        return jsonify({

            "mensaje":
            str(error)

        }),400


# ==========================================================
# CAMBIAR ESTADO ESTUDIANTE
# ==========================================================

@secretary_bp.route(
    "/students/<int:id>/status",
    methods=["PATCH"]
)
@jwt_required()
@requiere_rol("SECRETARIA")
def update_student_status(id):


    try:

        data = request.get_json()


        estudiante = cambiar_estado_estudiante(
            id,
            data["status"]
        )


        return jsonify({

            "mensaje":
            "Estado actualizado correctamente",


            "estudiante": {

                "id":
                estudiante.id,


                "codigo":
                estudiante.student_code,


                "estado":
                estudiante.status

            }

        })


    except ValueError as error:


        return jsonify({

            "mensaje":
            str(error)

        }),400

# ==========================================================
# IMPORTAR ESTUDIANTES EXCEL
# ==========================================================

@secretary_bp.route(
    "/students/import",
    methods=["POST"]
)
@jwt_required()
@requiere_rol("SECRETARIA")
def import_students():


    try:

        archivo = request.files.get(
            "file"
        )


        if not archivo:

            return jsonify({

                "mensaje":
                "Debe enviar un archivo Excel"

            }),400



        resultado = importar_estudiantes_excel(
            archivo
        )


        return jsonify({

            "mensaje":
            "Carga completada",

            "resultado":
            resultado

        })



    except ValueError as error:


        return jsonify({

            "mensaje":
            str(error)

        }),400

# ==========================================================
# LISTAR DOCENTES
# ==========================================================

@secretary_bp.route(
    "/teachers",
    methods=["GET"]
)
@jwt_required()
@requiere_rol("SECRETARIA")
def teachers():


    datos = listar_docentes()


    return jsonify({

        "docentes": datos

    })
# ==========================================================
# CREAR DOCENTE
# ==========================================================

@secretary_bp.route(
    "/teachers",
    methods=["POST"]
)
@jwt_required()
@requiere_rol("SECRETARIA")
def create_teacher():

    try:

        data = request.get_json()


        docente = crear_docente(data)


        return jsonify({

            "mensaje":
            "Docente creado correctamente",

            "docente": {

                "id": docente.id,

                "codigo": docente.teacher_code,

                "persona": {

                    "dni": docente.persona.dni,

                    "nombres": docente.persona.nombres,

                    "apellidos": docente.persona.apellidos

                }

            }

        }),201


    except ValueError as error:


        return jsonify({

            "mensaje": str(error)

        }),400

# ==========================================================
# ACTUALIZAR DOCENTE
# ==========================================================

@secretary_bp.route(
    "/teachers/<int:id>",
    methods=["PUT"]
)
@jwt_required()
@requiere_rol("SECRETARIA")
def update_teacher(id):


    try:

        data = request.get_json()


        docente = actualizar_docente(
            id,
            data
        )


        return jsonify({

            "mensaje":
            "Docente actualizado correctamente",


            "docente": {

                "id":
                docente.id,


                "codigo":
                docente.teacher_code,


                "persona": {

                    "nombres":
                    docente.persona.nombres,


                    "apellidos":
                    docente.persona.apellidos

                }

            }

        })


    except ValueError as error:


        return jsonify({

            "mensaje":
            str(error)

        }),400

# ==========================================================
# CAMBIAR ESTADO DOCENTE
# ==========================================================

@secretary_bp.route(
    "/teachers/<int:id>/status",
    methods=["PATCH"]
)
@jwt_required()
@requiere_rol("SECRETARIA")
def update_teacher_status(id):


    try:

        data = request.get_json()


        docente = cambiar_estado_docente(
            id,
            data["status"]
        )


        return jsonify({

            "mensaje":
            "Estado actualizado correctamente",


            "docente": {

                "id":
                docente.id,


                "codigo":
                docente.teacher_code,


                "estado":
                docente.status

            }

        })


    except ValueError as error:


        return jsonify({

            "mensaje":
            str(error)

        }),400

# ==========================================================
# IMPORTAR DOCENTES EXCEL
# ==========================================================

@secretary_bp.route(
    "/teachers/import",
    methods=["POST"]
)
@jwt_required()
@requiere_rol("SECRETARIA")
def import_teachers():


    try:

        archivo = request.files.get(
            "file"
        )


        if not archivo:

            return jsonify({

                "mensaje":
                "Debe enviar un archivo Excel"

            }),400



        resultado = importar_docentes_excel(
            archivo
        )


        return jsonify({

            "mensaje":
            "Carga completada",

            "resultado":
            resultado

        })


    except ValueError as error:


        return jsonify({

            "mensaje":
            str(error)

        }),400