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
    Matricula,
    AsignacionDocente,
    MatriculaEstudiante,
    AsignacionCurso,
    PeriodoAcademico,
    Seccion
)



app = create_app()



with app.app_context():


    print("==============================")
    print("MIGRANDO DATOS AL NUEVO DER")
    print("==============================")


    # ======================================
    # OBTENER PERIODO Y SECCION
    # ======================================

    periodo = PeriodoAcademico.query.filter_by(
        name="2026-I"
    ).first()


    seccion = Seccion.query.filter_by(
        name="A"
    ).first()


    if not periodo or not seccion:

        raise Exception(
            "No existe periodo o sección académica"
        )



    # ======================================
    # MIGRAR MATRICULAS
    # ======================================

    matriculas = Matricula.query.all()


    for matricula in matriculas:


        existe = MatriculaEstudiante.query.filter_by(
            student_id=matricula.student_id,
            academic_period_id=periodo.id,
            section_id=seccion.id
        ).first()


        if not existe:


            nueva = MatriculaEstudiante(

                student_id=matricula.student_id,

                academic_period_id=periodo.id,

                section_id=seccion.id,

                status=True

            )


            db.session.add(nueva)



    db.session.commit()



    print(
        "Matriculas migradas:",
        len(matriculas)
    )



    # ======================================
    # MIGRAR ASIGNACIONES DOCENTES
    # ======================================


    asignaciones = AsignacionDocente.query.all()


    for asignacion in asignaciones:


        existe = AsignacionCurso.query.filter_by(

            teacher_id=asignacion.teacher_id,

            course_id=asignacion.course_id,

            academic_period_id=periodo.id,

            section_id=seccion.id

        ).first()



        if not existe:


            nueva = AsignacionCurso(

                teacher_id=asignacion.teacher_id,

                course_id=asignacion.course_id,

                academic_period_id=periodo.id,

                section_id=seccion.id

            )


            db.session.add(nueva)



    db.session.commit()



    print(
        "Asignaciones migradas:",
        len(asignaciones)
    )



    print("==============================")
    print("MIGRACION COMPLETADA")
    print("==============================")