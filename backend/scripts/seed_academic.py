import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from app import create_app

from app.extensions.database import db


from app.modules.academic.models import (
    GradingScale,
    AnioAcademico,
    PeriodoAcademico,
    Grado,
    Seccion
)



app = create_app()



with app.app_context():


    print("==============================")
    print("CREANDO ESTRUCTURA ACADEMICA")
    print("==============================")


    # ===============================
    # ESCALA
    # ===============================

    escala = GradingScale.query.filter_by(
        name="Sistema vigesimal"
    ).first()


    if not escala:

        escala = GradingScale(

            name="Sistema vigesimal",

            minimum_value=0,

            maximum_value=20

        )

        db.session.add(escala)

        db.session.commit()



    # ===============================
    # AÑO
    # ===============================

    anio = AnioAcademico.query.filter_by(
        year=2026
    ).first()


    if not anio:

        anio = AnioAcademico(

            year=2026,

            grading_scale_id=escala.id

        )


        db.session.add(anio)

        db.session.commit()



    # ===============================
    # PERIODO
    # ===============================

    periodo = PeriodoAcademico.query.filter_by(
        name="2026-I"
    ).first()


    if not periodo:

        periodo = PeriodoAcademico(

            academic_year_id=anio.id,

            name="2026-I"

        )


        db.session.add(periodo)

        db.session.commit()



    # ===============================
    # GRADO
    # ===============================

    grado = Grado.query.filter_by(
        name="3° Secundaria"
    ).first()


    if not grado:

        grado = Grado(

            name="3° Secundaria",

            description="Tercer grado"

        )


        db.session.add(grado)

        db.session.commit()



    # ===============================
    # SECCION
    # ===============================

    seccion = Seccion.query.filter_by(
        name="A"
    ).first()


    if not seccion:

        seccion = Seccion(

            grade_level_id=grado.id,

            academic_year_id=anio.id,

            name="A"

        )


        db.session.add(seccion)

        db.session.commit()



    print("==============================")
    print("ESTRUCTURA CREADA")
    print("==============================")

    print(
        "Año:",
        anio.year
    )

    print(
        "Periodo:",
        periodo.name
    )

    print(
        "Grado:",
        grado.name
    )

    print(
        "Seccion:",
        seccion.name
    )