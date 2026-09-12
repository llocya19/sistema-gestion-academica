# ==========================================================
# MODELOS DEL MÓDULO ACADÉMICO
# Sistema de Gestión Académica con IA
#
# Contiene:
# - Personas
# - Estudiantes
# - Docentes
# - Cursos
# - Asignación docente-curso
#
# Estas tablas serán la base para:
# - indicadores académicos
# - análisis IA
# - rendimiento individual
# - rendimiento colectivo
# ==========================================================


from datetime import datetime

# Importamos SQLAlchemy
# Permite crear las tablas en PostgreSQL
from app.extensions.database import db



# ==========================================================
# TABLA: persons
#
# Guarda información general de una persona.
#
# Se crea para evitar duplicidad de datos.
#
# Ejemplo:
# Una misma persona puede ser:
# - estudiante
# - docente
#
# Relación:
#
# users 1 ----- 1 persons
#
# persons 1 ---- 1 students
#
# persons 1 ---- 1 teachers
# ==========================================================


class Person(db.Model):

    __tablename__ = "persons"


    # Identificador principal
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    # ==========================================================
    # RELACIÓN CON USUARIO DEL SISTEMA
    #
    # Permite enlazar:
    #
    # users
    #    |
    # persons
    #
    # Cada persona tiene una cuenta del sistema.
    # ==========================================================

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )


    # Documento de identidad
    dni = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )


    # Nombres de la persona
    first_name = db.Column(
        db.String(100),
        nullable=False
    )


    # Apellidos
    last_name = db.Column(
        db.String(100),
        nullable=False
    )


    # Número telefónico
    phone = db.Column(
        db.String(20)
    )


    # Dirección
    address = db.Column(
        db.String(200)
    )


    # Fecha de registro
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )





# ==========================================================
# TABLA: students
#
# Representa a los estudiantes del sistema.
#
# Guarda información académica,
# no información personal.
#
# Relación:
#
# persons 1 ----- 1 students
#
# Un estudiante pertenece a una persona.
# ==========================================================


class Student(db.Model):

    __tablename__ = "students"


    # Identificador del estudiante
    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # Persona asociada
    person_id = db.Column(
        db.Integer,
        db.ForeignKey("persons.id"),
        nullable=False,
        unique=True
    )


    # Código del estudiante
    # Ejemplo:
    # EST-2026-001
    student_code = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )


    # Estado del estudiante
    # activo / retirado
    status = db.Column(
        db.Boolean,
        default=True
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )





# ==========================================================
# TABLA: teachers
#
# Representa a los docentes.
#
# Relación:
#
# persons 1 ----- 1 teachers
#
# ==========================================================


class Teacher(db.Model):

    __tablename__ = "teachers"


    # Identificador docente
    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # Persona asociada
    person_id = db.Column(
        db.Integer,
        db.ForeignKey("persons.id"),
        nullable=False,
        unique=True
    )


    # Código docente
    # Ejemplo:
    # DOC-001
    teacher_code = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )


    # Estado del docente
    status = db.Column(
        db.Boolean,
        default=True
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )





# ==========================================================
# TABLA: courses
#
# Representa los cursos académicos.
#
# Ejemplo:
# - Matemática
# - Física
# - Programación
#
# ==========================================================


class Course(db.Model):

    __tablename__ = "courses"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # Código del curso
    # Ejemplo:
    # MAT101
    code = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )


    # Nombre del curso
    name = db.Column(
        db.String(150),
        nullable=False
    )


    # Descripción
    description = db.Column(
        db.String(250)
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )





# ==========================================================
# TABLA: teacher_courses
#
# Tabla intermedia entre docentes y cursos.
#
# Relación:
#
# teachers N ----- M courses
#
#
# Permite conocer:
#
# Qué docente dicta qué curso.
#
# Esta tabla será utilizada para calcular:
#
# Indicador docente-curso:
#
# porcentaje basado en las notas
# de todos sus estudiantes.
#
# ==========================================================


class TeacherCourse(db.Model):

    __tablename__ = "teacher_courses"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # Docente asignado
    teacher_id = db.Column(
        db.Integer,
        db.ForeignKey("teachers.id"),
        nullable=False
    )


    # Curso asignado
    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )