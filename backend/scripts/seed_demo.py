import sys
import os

from datetime import date

from werkzeug.security import generate_password_hash


# permitir importar app
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from app import create_app
from app.extensions.database import db


from app.modules.auth.models import (
    Rol,
    Usuario
)


from app.modules.academic.models import (
    Persona,
    Estudiante,
    Docente,
    Curso,
    AsignacionDocente,
    Matricula,
    Sesion,
    Tema,
    Evaluacion,
    Nota,
    Asistencia,
    Incidencia
)



app = create_app()



with app.app_context():


    print("================================")
    print("CREANDO DATOS DEMO")
    print("================================")


    # ==================================================
    # ROLES
    # ==================================================

    nombres_roles = [

        (
            "ADMINISTRADOR",
            "Administrador del sistema"
        ),

        (
            "DIRECTORA",
            "Dirección académica"
        ),

        (
            "SECRETARIA",
            "Gestión administrativa"
        ),

        (
            "DOCENTE",
            "Gestión académica docente"
        )

    ]


    for nombre, descripcion in nombres_roles:


        rol = Rol.query.filter_by(
            name=nombre
        ).first()


        if not rol:

            db.session.add(
                Rol(
                    name=nombre,
                    description=descripcion
                )
            )


    db.session.commit()



    # ==================================================
    # PERSONAS + USUARIOS
    # ==================================================

    usuarios_demo = [

        (
            "70000001",
            "Carlos",
            "Administrador",
            "admin@test.com",
            "ADMINISTRADOR"
        ),

        (
            "70000002",
            "Maria",
            "Directora",
            "directora@test.com",
            "DIRECTORA"
        ),

        (
            "70000003",
            "Ana",
            "Secretaria",
            "secretaria@test.com",
            "SECRETARIA"
        ),

        (
            "70000004",
            "Juan",
            "Profesor",
            "docente@test.com",
            "DOCENTE"
        )

    ]



    personas = {}



    for dni, nombres, apellidos, email, rol_nombre in usuarios_demo:


        usuario = Usuario.query.filter_by(
            email=email
        ).first()



        if not usuario:


            persona = Persona(

                dni=dni,

                nombres=nombres,

                apellidos=apellidos

            )


            db.session.add(persona)

            db.session.flush()



            rol = Rol.query.filter_by(
                name=rol_nombre
            ).first()



            usuario = Usuario(

                persona_id=persona.id,

                email=email,

                password_hash=generate_password_hash(
                    "123456"
                ),

                role_id=rol.id

            )


            db.session.add(usuario)



            personas[email] = persona



        else:

            personas[email] = usuario.persona



    db.session.commit()



    # ==================================================
    # ESTUDIANTES
    # ==================================================

    estudiantes_data = [

        (
            "80000001",
            "Pedro",
            "Perez",
            "EST001"
        ),

        (
            "80000002",
            "Lucia",
            "Gomez",
            "EST002"
        ),

        (
            "80000003",
            "Jose",
            "Lopez",
            "EST003"
        )

    ]



    estudiantes=[]


    for dni,nombres,apellidos,codigo in estudiantes_data:


        persona = Persona(

            dni=dni,

            nombres=nombres,

            apellidos=apellidos

        )


        db.session.add(persona)

        db.session.flush()



        estudiante = Estudiante(

            person_id=persona.id,

            student_code=codigo

        )


        db.session.add(estudiante)

        estudiantes.append(estudiante)



    db.session.commit()



    # ==================================================
    # DOCENTE
    # ==================================================

    persona_docente = personas[
        "docente@test.com"
    ]


    docente = Docente.query.filter_by(
        person_id=persona_docente.id
    ).first()



    if not docente:

        docente = Docente(

            person_id=persona_docente.id,

            teacher_code="DOC001"

        )


        db.session.add(docente)

        db.session.commit()



    # ==================================================
    # CURSOS
    # ==================================================

    cursos=[]


    cursos_data=[

        (
            "MAT101",
            "Matemática"
        ),

        (
            "PRO101",
            "Programación"
        ),

        (
            "BD101",
            "Base de Datos"
        )

    ]



    for codigo,nombre in cursos_data:


        curso = Curso(

            code=codigo,

            name=nombre,

            description="Curso académico"

        )


        db.session.add(curso)

        cursos.append(curso)



    db.session.commit()



    # ==================================================
    # ASIGNACION DOCENTE
    # ==================================================

    asignacion = AsignacionDocente(

        teacher_id=docente.id,

        course_id=cursos[0].id

    )


    db.session.add(asignacion)

    db.session.commit()



    # ==================================================
    # MATRICULAS
    # ==================================================

    for estudiante in estudiantes:


        db.session.add(

            Matricula(

                student_id=estudiante.id,

                course_id=cursos[0].id,

                academic_period="2026-I"

            )

        )


    db.session.commit()



    # ==================================================
    # SESION
    # ==================================================

    sesion = Sesion(

        teacher_course_id=asignacion.id,

        title="Introducción al curso",

        description="Primera sesión",

        session_date=date.today()

    )


    db.session.add(sesion)

    db.session.commit()



    # ==================================================
    # TEMA
    # ==================================================

    tema = Tema(

        session_id=sesion.id,

        name="Tema inicial",

        description="Conceptos básicos"

    )


    db.session.add(tema)



    # ==================================================
    # EVALUACION
    # ==================================================

    evaluacion = Evaluacion(

        teacher_course_id=asignacion.id,

        name="Examen parcial",

        evaluation_type="EXAMEN",

        evaluation_date=date.today()

    )


    db.session.add(evaluacion)

    db.session.commit()



    # ==================================================
    # NOTAS
    # ==================================================

    notas=[15,12,18]


    for estudiante,valor in zip(
        estudiantes,
        notas
    ):


        db.session.add(

            Nota(

                estudiante_id=estudiante.id,

                evaluacion_id=evaluacion.id,

                nota=valor

            )

        )


    db.session.commit()



    # ==================================================
    # ASISTENCIA
    # ==================================================

    for estudiante in estudiantes:


        db.session.add(

            Asistencia(

                sesion_id=sesion.id,

                estudiante_id=estudiante.id,

                estado="PRESENTE"

            )

        )


    db.session.commit()



    # ==================================================
    # INCIDENCIA
    # ==================================================

    db.session.add(

        Incidencia(

            estudiante_id=estudiantes[1].id,

            asignacion_docente_id=asignacion.id,

            tipo="BAJO RENDIMIENTO",

            descripcion="Necesita reforzamiento",

            gravedad="MEDIA",

            fecha_incidente=date.today(),

            tema_id=tema.id

        )

    )


    db.session.commit()



    print("==============================")
    print("DATOS DEMO CREADOS")
    print("==============================")