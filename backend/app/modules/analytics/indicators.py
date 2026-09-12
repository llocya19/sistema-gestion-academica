from app.extensions.database import db

from app.modules.academic.models import Grade
from app.modules.academic.models import Attendance
from app.modules.academic.models import Incident


# ==========================================================
# INDICADOR 1:
# CALCULAR PROMEDIO ACADÉMICO
#
# Obtiene todas las notas de un estudiante
# y calcula su promedio general.
#
# Fuente:
# tabla grades
#
# ==========================================================


def calcular_promedio_estudiante(student_id):

    notas = (
        db.session.query(Grade.grade)
        .filter(
            Grade.student_id == student_id
        )
        .all()
    )


    # Si no tiene notas registradas

    if not notas:
        return 0


    total = sum(
        float(nota[0])
        for nota in notas
    )


    promedio = total / len(notas)


    return round(promedio, 2)



# ==========================================================
# INDICADOR 2:
# CALCULAR PORCENTAJE DE ASISTENCIA
#
# Fuente:
# tabla attendance
#
# Fórmula:
#
# asistencias / total registros * 100
#
# ==========================================================


def calcular_asistencia_estudiante(student_id):


    registros = (
        db.session.query(Attendance)
        .filter(
            Attendance.student_id == student_id
        )
        .all()
    )


    if not registros:
        return 0


    presentes = 0


    for registro in registros:

        if registro.status == "PRESENTE":

            presentes += 1



    porcentaje = (
        presentes / len(registros)
    ) * 100


    return round(porcentaje, 2)



# ==========================================================
# INDICADOR 3:
# CONTAR INCIDENCIAS
#
# Fuente:
# tabla incidents
#
# ==========================================================


def contar_incidencias(student_id):


    cantidad = (
        db.session.query(Incident)
        .filter(
            Incident.student_id == student_id
        )
        .count()
    )


    return cantidad



# ==========================================================
# INDICADOR 4:
# NIVEL DE RIESGO ACADÉMICO
#
# Primera versión basada en reglas.
#
# Más adelante será reemplazada
# por un modelo IA.
#
# ==========================================================


def calcular_nivel_riesgo(
        promedio,
        asistencia,
        incidencias
):


    if (
        promedio < 11
        or asistencia < 60
        or incidencias >= 3
    ):

        return "ALTO"



    elif (
        promedio < 14
        or asistencia < 80
        or incidencias >= 1
    ):

        return "MEDIO"



    else:

        return "BAJO"