import sys
import os

from datetime import date


# Permite importar app desde scripts
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
    User,
    Role
)


from app.modules.academic.models import (
    Person,
    Student,
    Teacher,
    Course,
    TeacherCourse,
    Enrollment,
    Session,
    Topic,
    Evaluation,
    Grade,
    Attendance,
    Incident
)



app = create_app()



with app.app_context():


    print("Creando datos demo...")


    # ==========================
    # ROLES
    # ==========================


    role_student = Role.query.filter_by(
        name="ESTUDIANTE"
    ).first()


    if not role_student:

        role_student = Role(
            name="ESTUDIANTE",
            description="Usuario estudiante"
        )

        db.session.add(role_student)



    role_teacher = Role.query.filter_by(
        name="DOCENTE"
    ).first()


    if not role_teacher:

        role_teacher = Role(
            name="DOCENTE",
            description="Usuario docente"
        )

        db.session.add(role_teacher)


    db.session.commit()



    # ==========================
    # USUARIOS
    # ==========================


    user_student = User.query.filter_by(
        email="alumno@test.com"
    ).first()


    if not user_student:

        user_student = User(
            first_name="Carlos",
            last_name="Alumno",
            email="alumno@test.com",
            password_hash="123456",
            role_id=role_student.id
        )

        db.session.add(user_student)



    user_teacher = User.query.filter_by(
        email="docente@test.com"
    ).first()


    if not user_teacher:

        user_teacher = User(
            first_name="Juan",
            last_name="Profesor",
            email="docente@test.com",
            password_hash="123456",
            role_id=role_teacher.id
        )

        db.session.add(user_teacher)


    db.session.commit()



    # ==========================
    # PERSONAS
    # ==========================


    person_student = Person(

        user_id=user_student.id,

        dni="12345678",

        first_name="Carlos",

        last_name="Alumno"

    )


    person_teacher = Person(

        user_id=user_teacher.id,

        dni="87654321",

        first_name="Juan",

        last_name="Profesor"

    )


    db.session.add_all(
        [
            person_student,
            person_teacher
        ]
    )


    db.session.commit()



    # ==========================
    # ESTUDIANTE Y DOCENTE
    # ==========================


    student = Student(

        person_id=person_student.id,

        student_code="EST001"

    )


    teacher = Teacher(

        person_id=person_teacher.id,
        teacher_code="DOC001"

    )


    db.session.add_all(
        [
            student,
            teacher
        ]
    )


    db.session.commit()



    # ==========================
    # CURSO
    # ==========================


    course = Course(

        code="MAT101",

        name="Matemática",

        description="Curso básico"

    )


    db.session.add(course)

    db.session.commit()



    # ==========================
    # DOCENTE CURSO
    # ==========================


    teacher_course = TeacherCourse(

        teacher_id=teacher.id,

        course_id=course.id

    )


    db.session.add(teacher_course)

    db.session.commit()



    # ==========================
    # MATRICULA
    # ==========================


    enrollment = Enrollment(

        student_id=student.id,

        course_id=course.id,

        academic_period="2026-I"

    )


    db.session.add(enrollment)

    db.session.commit()



    # ==========================
    # SESION
    # ==========================


    session = Session(

        teacher_course_id=teacher_course.id,

        title="Clase inicial",

        description="Introducción",

        session_date=date.today()

    )


    db.session.add(session)

    db.session.commit()



    # ==========================
    # EVALUACION
    # ==========================


    evaluation = Evaluation(

        teacher_course_id=teacher_course.id,

        name="Examen parcial",

        evaluation_type="EXAMEN",

        evaluation_date=date.today()

    )


    db.session.add(evaluation)

    db.session.commit()



    # ==========================
    # NOTAS
    # ==========================


    db.session.add_all(

        [

            Grade(

                student_id=student.id,

                evaluation_id=evaluation.id,

                grade=15

            ),

            Grade(

                student_id=student.id,

                evaluation_id=evaluation.id,

                grade=13

            )

        ]

    )


    db.session.commit()



    # ==========================
    # ASISTENCIA
    # ==========================


    db.session.add(

        Attendance(

            session_id=session.id,

            student_id=student.id,

            status="PRESENTE"

        )

    )


    db.session.commit()



    # ==========================
    # INCIDENCIA
    # ==========================


    db.session.add(

        Incident(

            student_id=student.id,

            teacher_course_id=teacher_course.id,

            type="BAJO RENDIMIENTO",

            description="Necesita reforzamiento",

            severity="MEDIA",

            incident_date=date.today()

        )

    )


    db.session.commit()



    print("==============================")
    print("DATOS DEMO CREADOS")
    print("Estudiante:", student.id)
    print("Curso:", course.id)
    print("==============================")