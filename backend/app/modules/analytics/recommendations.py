def generar_recomendaciones(
        promedio,
        asistencia,
        incidencias
):

    recomendaciones = []


    if promedio < 11:

        recomendaciones.append({

            "categoria": "RENDIMIENTO",

            "mensaje":
            "El estudiante presenta bajo rendimiento académico. Se recomienda reforzar los temas con menor desempeño."

        })


    if asistencia < 70:

        recomendaciones.append({

            "categoria": "ASISTENCIA",

            "mensaje":
            "La asistencia del estudiante es baja. Se recomienda revisar las causas de inasistencia."

        })


    if incidencias >= 3:

        recomendaciones.append({

            "categoria": "INCIDENCIAS",

            "mensaje":
            "Se detectaron varias incidencias académicas. Se recomienda intervención del docente."

        })


    if len(recomendaciones) == 0:

        recomendaciones.append({

            "categoria": "GENERAL",

            "mensaje":
            "El estudiante mantiene un desempeño adecuado."

        })


    return recomendaciones