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

# ==========================================================
# TABLA: enrollments
#
# Representa la matrícula de un estudiante
# dentro de un curso académico.
#
# Relación:
#
# students N ----- M courses
#
# Esta tabla será utilizada para:
# - notas
# - asistencia
# - incidencias
# - análisis IA
# ==========================================================


class Enrollment(db.Model):

    __tablename__ = "enrollments"


    # Identificador de matrícula
    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # Estudiante matriculado
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )


    # Curso donde está matriculado
    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )


    # Periodo académico
    # Ejemplo:
    # 2026-I
    academic_period = db.Column(
        db.String(20),
        nullable=False
    )


    # Estado:
    # activo
    # retirado
    status = db.Column(
        db.Boolean,
        default=True
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Evita matrículas duplicadas
    # Un estudiante no puede estar
    # dos veces en el mismo curso
    # durante el mismo periodo académico

    __table_args__ = (
        db.UniqueConstraint(
            "student_id",
            "course_id",
            "academic_period",
            name="unique_student_course_period"
        ),
    )

# ==========================================================
# TABLA: sessions
#
# Registra las sesiones de clase realizadas por el docente.
#
# Relación:
#
# teacher_courses 1 ----- N sessions
#
# Una asignación docente-curso puede tener
# muchas sesiones.
#
# Ejemplo:
#
# Docente:
# Juan Pérez
#
# Curso:
# Matemática
#
# Sesiones:
# - Semana 1: Funciones
# - Semana 2: Límites
#
# Esta tabla permite a la directora verificar
# la trazabilidad de la enseñanza.
# ==========================================================


class Session(db.Model):

    __tablename__ = "sessions"


    # Identificador de sesión
    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # Relación con docente-curso
    #
    # Indica qué docente dictó
    # esta sesión y en qué curso.
    teacher_course_id = db.Column(
        db.Integer,
        db.ForeignKey("teacher_courses.id"),
        nullable=False
    )


    # Nombre de la sesión
    # Ejemplo:
    # Introducción a derivadas
    title = db.Column(
        db.String(150),
        nullable=False
    )


    # Descripción de lo realizado
    description = db.Column(
        db.Text
    )


    # Fecha en la que se realizó la sesión
    session_date = db.Column(
        db.Date,
        nullable=False
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
# ==========================================================
# TABLA: topics
#
# Representa los temas desarrollados dentro
# de una sesión.
#
# Relación:
#
# sessions 1 ----- N topics
#
# Ejemplo:
#
# Sesión:
# Derivadas
#
# Temas:
# - Concepto de derivada
# - Reglas de derivación
#
# Estos datos serán utilizados por la IA
# para relacionar dificultades académicas
# con temas específicos.
# ==========================================================


class Topic(db.Model):

    __tablename__ = "topics"


    # Identificador del tema
    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # Sesión donde se enseñó el tema
    session_id = db.Column(
        db.Integer,
        db.ForeignKey("sessions.id"),
        nullable=False
    )


    # Nombre del tema
    name = db.Column(
        db.String(150),
        nullable=False
    )


    # Descripción del tema
    description = db.Column(
        db.Text
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

# ==========================================================
# TABLA: evaluations
#
# Registra las evaluaciones realizadas por el docente.
#
# IMPORTANTE:
#
# El examen es físico.
# El sistema NO almacena preguntas ni respuestas.
#
# Solo registra:
# - información de la evaluación
# - fecha
# - evidencia del examen
#
# Relación:
#
# teacher_courses 1 ----- N evaluations
#
# ==========================================================


class Evaluation(db.Model):

    __tablename__ = "evaluations"


    # Identificador de evaluación
    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # Curso y docente responsable
    teacher_course_id = db.Column(
        db.Integer,
        db.ForeignKey("teacher_courses.id"),
        nullable=False
    )


    # Nombre de evaluación
    # Ejemplo:
    # Examen Parcial 1
    # Examen Final
    name = db.Column(
        db.String(150),
        nullable=False
    )


    # Tipo:
    # parcial
    # final
    # práctica
    # tarea
    evaluation_type = db.Column(
        db.String(50),
        nullable=False
    )


    # Fecha realizada
    evaluation_date = db.Column(
        db.Date,
        nullable=False
    )


    # Evidencia del examen físico
    # Ruta de la imagen almacenada
    evidence_url = db.Column(
        db.String(255),
        nullable=True
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

# ==========================================================
# TABLA: evaluation_topics
#
# Relación muchos a muchos entre:
#
# evaluaciones
#        |
#        |
# temas evaluados
#
# Permite saber qué temas fueron evaluados
# en cada examen.
#
# ==========================================================


class EvaluationTopic(db.Model):

    __tablename__ = "evaluation_topics"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    evaluation_id = db.Column(
        db.Integer,
        db.ForeignKey("evaluations.id"),
        nullable=False
    )


    topic_id = db.Column(
        db.Integer,
        db.ForeignKey("topics.id"),
        nullable=False
    )

# ==========================================================
# TABLA: grades
#
# Guarda la nota obtenida por cada estudiante
# en una evaluación.
#
# Esta tabla será usada para:
#
# - promedio individual
# - promedio del curso
# - indicador docente-curso
# - análisis IA
#
# ==========================================================


class Grade(db.Model):

    __tablename__ = "grades"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # Estudiante evaluado
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )


    # Evaluación realizada
    evaluation_id = db.Column(
        db.Integer,
        db.ForeignKey("evaluations.id"),
        nullable=False
    )


    # Nota global del examen físico
    grade = db.Column(
        db.Numeric(5,2),
        nullable=False
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

# ==========================================================
# TABLA: attendance
#
# Registra la asistencia de los estudiantes
# durante una sesión de clase.
#
# Relación:
#
# sessions 1 ----- N attendance
#
# students 1 ----- N attendance
#
# Esta información será usada por la IA
# para calcular indicadores de asistencia.
# ==========================================================


class Attendance(db.Model):

    __tablename__ = "attendance"


    # Identificador
    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # Sesión de clase
    session_id = db.Column(
        db.Integer,
        db.ForeignKey("sessions.id"),
        nullable=False
    )


    # Estudiante
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )


    # Estado de asistencia
    #
    # PRESENTE
    # FALTA
    # TARDANZA
    # JUSTIFICADO

    status = db.Column(
        db.String(20),
        nullable=False
    )


    # Observación del docente
    observation = db.Column(
        db.Text
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

# ==========================================================
# TABLA: incidents
#
# Registra situaciones que afectan
# el rendimiento académico.
#
# Ejemplos:
#
# - Bajo rendimiento
# - Inasistencia frecuente
# - Dificultad en un tema
#
# Será utilizado por la IA para encontrar
# causas del bajo rendimiento.
# ==========================================================


class Incident(db.Model):

    __tablename__ = "incidents"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # Estudiante involucrado
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )


    # Curso donde ocurre
    teacher_course_id = db.Column(
        db.Integer,
        db.ForeignKey("teacher_courses.id"),
        nullable=False
    )


    # Tipo de incidencia
    #
    # Bajo rendimiento
    # Inasistencia
    # Dificultad temática

    type = db.Column(
        db.String(100),
        nullable=False
    )


    # Detalle de la incidencia
    description = db.Column(
        db.Text,
        nullable=False
    )


    # Baja
    # Media
    # Alta

    severity = db.Column(
        db.String(20),
        nullable=False
    )


    incident_date = db.Column(
        db.Date,
        nullable=False
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )