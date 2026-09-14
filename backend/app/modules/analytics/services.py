from app.extensions.database import db


from app.modules.analytics.models import (
    AnalisisIA,
    RecomendacionIA
)


from app.modules.analytics.indicators import (
    calcular_promedio_estudiante,
    calcular_asistencia_estudiante,
    contar_incidencias,
    calcular_nivel_riesgo
)


from app.modules.analytics.recommendations import (
    generar_recomendaciones
)



def generar_indicador_estudiante(estudiante_id):


    promedio = calcular_promedio_estudiante(
        estudiante_id
    )


    asistencia = calcular_asistencia_estudiante(
        estudiante_id
    )


    incidencias = contar_incidencias(
        estudiante_id
    )


    riesgo = calcular_nivel_riesgo(
        promedio,
        asistencia,
        incidencias
    )


    recomendaciones = generar_recomendaciones(
        promedio,
        asistencia,
        incidencias
    )


    return {

        "estudiante_id": estudiante_id,

        "promedio": promedio,

        "asistencia": asistencia,

        "incidencias": incidencias,

        "riesgo": riesgo,

        "recomendaciones": recomendaciones

    }



def guardar_indicador_estudiante(estudiante_id):


    resultado = generar_indicador_estudiante(
        estudiante_id
    )


    indicador = AnalisisIA(

        estudiante_id=estudiante_id,

        promedio=resultado["promedio"],

        porcentaje_asistencia=resultado["asistencia"],

        cantidad_incidencias=resultado["incidencias"],

        nivel_riesgo=resultado["riesgo"]

    )


    db.session.add(indicador)



    for item in resultado["recomendaciones"]:


        recomendacion = RecomendacionIA(

            estudiante_id=estudiante_id,

            categoria=item["categoria"],

            mensaje=item["mensaje"]

        )


        db.session.add(
            recomendacion
        )



    db.session.commit()



    resultado["guardado"] = True


    return resultado