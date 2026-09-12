# ==========================================================
# SERVICIOS DE ANALISIS ACADEMICO
#
# Este archivo combina los indicadores calculados
# para generar un resumen completo del estudiante.
#
# ==========================================================


from app.modules.analytics.indicators import (
    calcular_promedio_estudiante,
    calcular_asistencia_estudiante,
    contar_incidencias,
    calcular_nivel_riesgo
)



# ==========================================================
# GENERAR INDICADOR DEL ESTUDIANTE
#
# Integra:
#
# - Promedio académico
# - Porcentaje asistencia
# - Cantidad de incidencias
# - Nivel de riesgo
#
# ==========================================================


def generar_indicador_estudiante(student_id):


    promedio = calcular_promedio_estudiante(
        student_id
    )


    asistencia = calcular_asistencia_estudiante(
        student_id
    )


    incidencias = contar_incidencias(
        student_id
    )


    riesgo = calcular_nivel_riesgo(
        promedio,
        asistencia,
        incidencias
    )


    return {

        "student_id": student_id,

        "promedio": promedio,

        "asistencia": asistencia,

        "incidencias": incidencias,

        "riesgo": riesgo

    }