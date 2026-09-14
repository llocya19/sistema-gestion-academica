from sqlalchemy import func

from app.extensions.database import db

from app.modules.academic.models import (
    Estudiante,
    Nota,
    Asistencia,
    Incidencia
)



# ==========================================================
# PROMEDIO DEL ESTUDIANTE
# ==========================================================


def calcular_promedio_estudiante(estudiante_id):

    resultado = db.session.query(
        func.avg(
            Nota.nota
        )
    ).filter(
        Nota.estudiante_id == estudiante_id
    ).scalar()


    if resultado is None:
        return 0


    return float(resultado)



# ==========================================================
# PORCENTAJE DE ASISTENCIA
# ==========================================================


def calcular_asistencia_estudiante(estudiante_id):

    total = Asistencia.query.filter_by(
        estudiante_id=estudiante_id
    ).count()


    if total == 0:
        return 0


    presentes = Asistencia.query.filter_by(
        estudiante_id=estudiante_id,
        estado="PRESENTE"
    ).count()


    return round(
        (presentes / total) * 100,
        2
    )



# ==========================================================
# CONTAR INCIDENCIAS
# ==========================================================


def contar_incidencias(estudiante_id):

    return Incidencia.query.filter_by(
        estudiante_id=estudiante_id
    ).count()



# ==========================================================
# NIVEL DE RIESGO
# ==========================================================


def calcular_nivel_riesgo(
        promedio,
        asistencia,
        incidencias
):


    if promedio < 11:
        return "ALTO"


    if asistencia < 70:
        return "ALTO"


    if incidencias >= 3:
        return "ALTO"


    if promedio < 14:
        return "MEDIO"


    if asistencia < 85:
        return "MEDIO"


    if incidencias > 0:
        return "MEDIO"


    return "BAJO"