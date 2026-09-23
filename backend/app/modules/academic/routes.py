from flask import Blueprint, jsonify, request


from app.modules.academic.services import (
    listar_anios,
    crear_anio,
    listar_periodos,
    crear_periodo,
    listar_grados,
    crear_grado,
    listar_secciones,
    crear_seccion,
    listar_asignaciones,
    crear_asignacion,
    listar_cursos,
    crear_curso,
)

academic_bp = Blueprint(
    "academic",
    __name__,
    url_prefix="/api/academic"
)



@academic_bp.route(
    "/test",
    methods=["GET"]
)
def academic_test():

    return jsonify({

        "mensaje":
        "Modulo académico funcionando"

    })

# ==========================================================
# LISTAR AÑOS ACADÉMICOS
# ==========================================================

@academic_bp.route(
    "/years",
    methods=["GET"]
)
def years():


    datos = listar_anios()


    return jsonify({

        "años": datos

    })
# ==========================================================
# CREAR AÑO ACADÉMICO
# ==========================================================

@academic_bp.route(
    "/years",
    methods=["POST"]
)
def create_year():


    try:

        data = request.get_json()


        anio = crear_anio(data)


        return jsonify({

            "mensaje":
            "Año académico creado correctamente",

            "anio": {

                "id": anio.id,

                "year": anio.year,

                "estado": anio.status

            }

        }),201


    except ValueError as error:


        return jsonify({

            "mensaje": str(error)

        }),400

# ==========================================================
# LISTAR PERIDO ACADÉMICOS
# ==========================================================
@academic_bp.route(
    "/periods",
    methods=["GET"]
)
def periods():

    datos = listar_periodos()

    return jsonify({

        "periodos": datos

    })
# ==========================================================
# CREAR PERIODO ACADÉMICO
# =================================================
@academic_bp.route(
    "/periods",
    methods=["POST"]
)
def create_period():


    try:

        data = request.get_json()


        periodo = crear_periodo(data)


        return jsonify({

            "mensaje":
            "Periodo académico creado correctamente",

            "periodo": {

                "id": periodo.id,

                "nombre": periodo.name

            }

        }),201


    except ValueError as error:


        return jsonify({

            "mensaje": str(error)

        }),400


# ==========================================================
# LISTAR GRADOS ACADÉMICOS
# =================================================
@academic_bp.route(
    "/grades",
    methods=["GET"]
)
def grades():


    datos = listar_grados()


    return jsonify({

        "grados": datos

    })
# ==========================================================
# CREAR GRADOS ACADÉMICOS
# =================================================
@academic_bp.route(
    "/grades",
    methods=["POST"]
)
def create_grade():


    try:

        data = request.get_json()


        grado = crear_grado(data)


        return jsonify({

            "mensaje":
            "Grado creado correctamente",

            "grado": {

                "id": grado.id,

                "nombre": grado.name,

                "descripcion": grado.description

            }

        }),201


    except ValueError as error:


        return jsonify({

            "mensaje": str(error)

        }),400


# ==========================================================
# LISTAR seccion ACADÉMICOS
# =================================================
@academic_bp.route(
    "/sections",
    methods=["GET"]
)
def sections():

    datos = listar_secciones()


    return jsonify({

        "secciones": datos

    })
# ==========================================================
# crear seccion ACADÉMICOS
# =================================================
@academic_bp.route(
    "/sections",
    methods=["POST"]
)
def create_section():

    try:

        data = request.get_json()


        seccion = crear_seccion(data)


        return jsonify({

            "mensaje":
            "Sección creada correctamente",

            "seccion": {

                "id": seccion.id,

                "nombre": seccion.name

            }

        }),201


    except ValueError as error:


        return jsonify({

            "mensaje": str(error)

        }),400

# ==========================================================
# LISTAR Asignacion ACADÉMICOS
# ===========================
@academic_bp.route(
    "/assignments",
    methods=["GET"]
)
def assignments():

    datos = listar_asignaciones()

    return jsonify({

        "asignaciones": datos

    })
# ==========================================================
# Crear Asignacion ACADÉMICOS
# ===========================
@academic_bp.route(
    "/assignments",
    methods=["POST"]
)
def create_assignment():

    try:

        data = request.get_json()

        asignacion = crear_asignacion(data)


        return jsonify({

            "mensaje":
            "Asignación creada correctamente",

            "id":
            asignacion.id

        }),201


    except ValueError as error:

        return jsonify({

            "mensaje": str(error)

        }),400

# ==========================================================
# LISTAR CURSOS
# ==========================================================

@academic_bp.route(
    "/courses",
    methods=["GET"]
)
def courses():


    datos = listar_cursos()


    return jsonify({

        "cursos": datos

    })
# ==========================================================
# CREAR CURSO
# ==========================================================

@academic_bp.route(
    "/courses",
    methods=["POST"]
)
def create_course():


    try:

        data = request.get_json()


        curso = crear_curso(data)


        return jsonify({

            "mensaje":
            "Curso creado correctamente",


            "curso": {

                "id": curso.id,

                "nombre": curso.name,

                "codigo": curso.code

            }

        }),201


    except ValueError as error:


        return jsonify({

            "mensaje": str(error)

        }),400