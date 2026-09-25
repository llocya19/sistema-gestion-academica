from app.extensions.database import db

from app.modules.academic.models import (
    AnioAcademico,
    PeriodoAcademico,
    Grado,
    Seccion,
    Curso,
    AsignacionCurso
)
# ==========================================================
# LISTAR AÑOS ACADÉMICOS
# ==========================================================

def listar_anios():

    anios = AnioAcademico.query.all()

    resultado = []


    for anio in anios:

        resultado.append({

            "id": anio.id,

            "anio": anio.year,

            "estado": anio.status

        })


    return resultado



# ==========================================================
# CREAR AÑO ACADÉMICO
# ==========================================================

def crear_anio(data):


    anio_existente = AnioAcademico.query.filter_by(
        year=data["year"]
    ).first()


    if anio_existente:

        raise ValueError(
            "El año académico ya existe"
        )


    anio = AnioAcademico(

        year=data["year"],

        status=True

    )


    db.session.add(anio)

    db.session.commit()


    return anio

# ==========================================================
# LISTAR PERIODOS ACADÉMICOS
# ==========================================================

def listar_periodos():

    periodos = PeriodoAcademico.query.all()

    resultado = []


    for periodo in periodos:

        resultado.append({

            "id": periodo.id,

            "nombre": periodo.name,

            "fecha_inicio": str(periodo.start_date),

            "fecha_fin": str(periodo.end_date),

            "anio_academico": periodo.academic_year_id

        })


    return resultado



# ==========================================================
# CREAR PERIODO ACADÉMICO
# ==========================================================

def crear_periodo(data):


    anio = AnioAcademico.query.get(
        data["academic_year_id"]
    )


    if not anio:

        raise ValueError(
            "El año académico no existe"
        )


    periodo = PeriodoAcademico(

        academic_year_id=data["academic_year_id"],

        name=data["name"],

        start_date=data["start_date"],

        end_date=data["end_date"]

    )


    db.session.add(periodo)

    db.session.commit()


    return periodo
# ==========================================================
# LISTAR GRADOS
# ==========================================================

def listar_grados():

    grados = Grado.query.all()

    resultado = []


    for grado in grados:

        resultado.append({

            "id": grado.id,

            "nombre": grado.name,

            "descripcion": grado.description

        })


    return resultado



# ==========================================================
# CREAR GRADO
# ==========================================================

def crear_grado(data):


    grado_existente = Grado.query.filter_by(
        name=data["name"]
    ).first()


    if grado_existente:

        raise ValueError(
            "El grado ya existe"
        )


    grado = Grado(

        name=data["name"],

        description=data.get(
            "description"

        )

    )


    db.session.add(grado)

    db.session.commit()


    return grado

# ==========================================================
# LISTAR SECCIONES
# ==========================================================

def listar_secciones():

    secciones = Seccion.query.all()

    resultado = []


    for seccion in secciones:

        resultado.append({

            "id": seccion.id,

            "nombre": seccion.name,

            "grado": seccion.grado.name,

            "anio_academico": seccion.anio_academico.year

        })


    return resultado



# ==========================================================
# CREAR SECCION
# ==========================================================

def crear_seccion(data):


    grado = Grado.query.get(
        data["grade_level_id"]
    )


    if not grado:

        raise ValueError(
            "El grado no existe"
        )


    anio = AnioAcademico.query.get(
        data["academic_year_id"]
    )


    if not anio:

        raise ValueError(
            "El año académico no existe"
        )


    existe = Seccion.query.filter_by(

        grade_level_id=data["grade_level_id"],

        academic_year_id=data["academic_year_id"],

        name=data["name"]

    ).first()


    if existe:

        raise ValueError(
            "La sección ya existe para este grado y año"
        )


    seccion = Seccion(

        grade_level_id=data["grade_level_id"],

        academic_year_id=data["academic_year_id"],

        name=data["name"]

    )


    db.session.add(seccion)

    db.session.commit()


    return seccion

# ==========================================================
# LISTAR CURSOS
# ==========================================================

def listar_cursos():

    cursos = Curso.query.all()

    resultado = []


    for curso in cursos:

        resultado.append({

            "id": curso.id,

            "nombre": curso.name,

            "codigo": curso.code,

            "descripcion": curso.description

        })


    return resultado
# ==========================================================
# CREAR CURSO
# ==========================================================

def crear_curso(data):


    curso_existente = Curso.query.filter_by(
        code=data["code"]
    ).first()


    if curso_existente:

        raise ValueError(
            "El código del curso ya existe"
        )


    curso = Curso(

        name=data["name"],

        code=data["code"],

        description=data.get(
            "description"
        )

    )


    db.session.add(curso)

    db.session.commit()


    return curso
# ==========================================================
# LISTAR ASIGNACIONES DE CURSO
# ==========================================================

def listar_asignaciones():

    asignaciones = AsignacionCurso.query.all()

    resultado = []


    for asignacion in asignaciones:

        resultado.append({

            "id": asignacion.id,

            "docente": (
                asignacion.docente.persona.nombres
                + " "
                + asignacion.docente.persona.apellidos
            ),

            "curso": asignacion.curso.name,

            "periodo": asignacion.periodo.name,

            "seccion": asignacion.seccion.name

        })


    return resultado



# ==========================================================
# CREAR ASIGNACION
# ==========================================================

def crear_asignacion(data):


    existe = AsignacionCurso.query.filter_by(

        teacher_id=data["teacher_id"],

        course_id=data["course_id"],

        academic_period_id=data["academic_period_id"],

        section_id=data["section_id"]

    ).first()


    if existe:

        raise ValueError(
            "La asignación ya existe"
        )


    asignacion = AsignacionCurso(

        teacher_id=data["teacher_id"],

        course_id=data["course_id"],

        academic_period_id=data["academic_period_id"],

        section_id=data["section_id"]

    )


    db.session.add(asignacion)

    db.session.commit()


    return asignacion