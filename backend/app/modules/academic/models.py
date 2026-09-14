from datetime import datetime

from app.extensions.database import db



# ==========================================================
# TABLA: persons
#
# Información general de una persona.
#
# Una persona puede ser:
# - estudiante
# - docente
#
# Mantiene la normalización del DER.
#
# ==========================================================


class Persona(db.Model):

    __tablename__ = "persons"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # Relación con usuario del sistema

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )


    dni = db.Column(
        db.String(20),
        nullable=False,
        unique=True
    )


    nombres = db.Column(
        db.String(100),
        nullable=False
    )


    apellidos = db.Column(
        db.String(100),
        nullable=False
    )


    telefono = db.Column(
        db.String(20)
    )


    direccion = db.Column(
        db.String(200)
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    usuario = db.relationship(
        "Usuario",
        backref="persona",
        uselist=False
    )



# ==========================================================
# TABLA: students
#
# Información académica del estudiante.
#
# Los datos personales están en Persona.
#
# ==========================================================


class Estudiante(db.Model):

    __tablename__ = "students"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    person_id = db.Column(
        db.Integer,
        db.ForeignKey("persons.id"),
        nullable=False,
        unique=True
    )


    codigo_estudiante = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )


    estado = db.Column(
        db.Boolean,
        default=True
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    persona = db.relationship(
        "Persona",
        backref="estudiante",
        uselist=False
    )



# ==========================================================
# TABLA: teachers
#
# Información académica del docente.
#
# ==========================================================


class Docente(db.Model):

    __tablename__ = "teachers"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    person_id = db.Column(
        db.Integer,
        db.ForeignKey("persons.id"),
        nullable=False,
        unique=True
    )


    codigo_docente = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )


    estado = db.Column(
        db.Boolean,
        default=True
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    persona = db.relationship(
        "Persona",
        backref="docente",
        uselist=False
    )

# ==========================================================
# TABLA: courses
#
# Representa los cursos académicos.
#
# Ejemplo:
# Matemática
# Física
# Programación
#
# ==========================================================


class Curso(db.Model):

    __tablename__ = "courses"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    codigo = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )


    nombre = db.Column(
        db.String(150),
        nullable=False
    )


    descripcion = db.Column(
        db.String(250)
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )



# ==========================================================
# TABLA: teacher_courses
#
# Relación entre docentes y cursos.
#
# Permite saber:
#
# Qué docente dicta qué curso.
#
# ==========================================================


class AsignacionDocente(db.Model):

    __tablename__ = "teacher_courses"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    docente_id = db.Column(
        db.Integer,
        db.ForeignKey("teachers.id"),
        nullable=False
    )


    curso_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    docente = db.relationship(
        "Docente",
        backref="asignaciones"
    )


    curso = db.relationship(
        "Curso",
        backref="asignaciones"
    )


    __table_args__ = (

        db.UniqueConstraint(
            "docente_id",
            "curso_id",
            name="unique_docente_curso"
        ),

    )



# ==========================================================
# TABLA: enrollments
#
# Matrícula del estudiante en un curso.
#
# Relación:
#
# Estudiante N ----- M Curso
#
# ==========================================================


class Matricula(db.Model):

    __tablename__ = "enrollments"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    estudiante_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )


    curso_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )


    periodo_academico = db.Column(
        db.String(20),
        nullable=False
    )


    estado = db.Column(
        db.Boolean,
        default=True
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    estudiante = db.relationship(
        "Estudiante",
        backref="matriculas"
    )


    curso = db.relationship(
        "Curso",
        backref="matriculas"
    )


    __table_args__ = (

        db.UniqueConstraint(
            "estudiante_id",
            "curso_id",
            "periodo_academico",
            name="unique_estudiante_curso_periodo"
        ),

    )



# ==========================================================
# TABLA: sessions
#
# Registra las clases realizadas.
#
# Una asignación docente-curso
# puede tener muchas sesiones.
#
# ==========================================================


class Sesion(db.Model):

    __tablename__ = "sessions"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    asignacion_docente_id = db.Column(
        db.Integer,
        db.ForeignKey("teacher_courses.id"),
        nullable=False
    )


    titulo = db.Column(
        db.String(150),
        nullable=False
    )


    descripcion = db.Column(
        db.Text
    )


    fecha_sesion = db.Column(
        db.Date,
        nullable=False
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    asignacion_docente = db.relationship(
        "AsignacionDocente",
        backref="sesiones"
    )



# ==========================================================
# TABLA: topics
#
# Temas desarrollados dentro de una sesión.
#
# La IA utilizará esta información para relacionar:
#
# estudiante + evaluación + tema
#
# ==========================================================


class Tema(db.Model):

    __tablename__ = "topics"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    sesion_id = db.Column(
        db.Integer,
        db.ForeignKey("sessions.id"),
        nullable=False
    )


    nombre = db.Column(
        db.String(150),
        nullable=False
    )


    descripcion = db.Column(
        db.Text
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    sesion = db.relationship(
        "Sesion",
        backref="temas"
    )



# ==========================================================
# TABLA: evaluations
#
# Registra evaluaciones.
#
# El examen puede ser físico.
#
# Solo almacenamos:
# - datos del examen
# - fecha
# - evidencia
#
# ==========================================================


class Evaluacion(db.Model):

    __tablename__ = "evaluations"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    asignacion_docente_id = db.Column(
        db.Integer,
        db.ForeignKey("teacher_courses.id"),
        nullable=False
    )


    nombre = db.Column(
        db.String(150),
        nullable=False
    )


    tipo_evaluacion = db.Column(
        db.String(50),
        nullable=False
    )


    fecha_evaluacion = db.Column(
        db.Date,
        nullable=False
    )


    evidencia_url = db.Column(
        db.String(255)
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    asignacion_docente = db.relationship(
        "AsignacionDocente",
        backref="evaluaciones"
    )



# ==========================================================
# TABLA: evaluation_topics
#
# Relación:
#
# Evaluación N ----- M Tema
#
# Permite saber qué temas
# fueron evaluados.
#
# ==========================================================


class EvaluacionTema(db.Model):

    __tablename__ = "evaluation_topics"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    evaluacion_id = db.Column(
        db.Integer,
        db.ForeignKey("evaluations.id"),
        nullable=False
    )


    tema_id = db.Column(
        db.Integer,
        db.ForeignKey("topics.id"),
        nullable=False
    )


    evaluacion = db.relationship(
        "Evaluacion",
        backref="temas_evaluados"
    )


    tema = db.relationship(
        "Tema",
        backref="evaluaciones"
    )


    __table_args__ = (

        db.UniqueConstraint(
            "evaluacion_id",
            "tema_id",
            name="unique_evaluacion_tema"
        ),

    )

# ==========================================================
# TABLA: grades
#
# Guarda las notas obtenidas por los estudiantes.
#
# Utilizada para:
# - promedio individual
# - promedio curso
# - indicadores IA
#
# ==========================================================


class Nota(db.Model):

    __tablename__ = "grades"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    estudiante_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )


    evaluacion_id = db.Column(
        db.Integer,
        db.ForeignKey("evaluations.id"),
        nullable=False
    )


    nota = db.Column(
        db.Numeric(5,2),
        nullable=False
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    estudiante = db.relationship(
        "Estudiante",
        backref="notas"
    )


    evaluacion = db.relationship(
        "Evaluacion",
        backref="notas"
    )



# ==========================================================
# TABLA: attendance
#
# Registra asistencia por sesión.
#
# ==========================================================


class Asistencia(db.Model):

    __tablename__ = "attendance"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    sesion_id = db.Column(
        db.Integer,
        db.ForeignKey("sessions.id"),
        nullable=False
    )


    estudiante_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )


    estado = db.Column(
        db.String(20),
        nullable=False
    )


    observacion = db.Column(
        db.Text
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    sesion = db.relationship(
        "Sesion",
        backref="asistencias"
    )


    estudiante = db.relationship(
        "Estudiante",
        backref="asistencias"
    )



# ==========================================================
# TABLA: incidents
#
# Registra problemas académicos.
#
# Ejemplos:
# - bajo rendimiento
# - dificultad temática
# - inasistencia
#
# ==========================================================


class Incidencia(db.Model):

    __tablename__ = "incidents"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    estudiante_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )


    asignacion_docente_id = db.Column(
        db.Integer,
        db.ForeignKey("teacher_courses.id"),
        nullable=False
    )


    # NUEVO:
    # Relación directa con el tema donde aparece
    # la dificultad del estudiante.

    tema_id = db.Column(
        db.Integer,
        db.ForeignKey("topics.id"),
        nullable=True
    )


    tipo = db.Column(
        db.String(100),
        nullable=False
    )


    descripcion = db.Column(
        db.Text,
        nullable=False
    )


    gravedad = db.Column(
        db.String(20),
        nullable=False
    )


    fecha_incidente = db.Column(
        db.Date,
        nullable=False
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    estudiante = db.relationship(
        "Estudiante",
        backref="incidencias"
    )


    asignacion_docente = db.relationship(
        "AsignacionDocente",
        backref="incidencias"
    )


    tema = db.relationship(
        "Tema",
        backref="incidencias"
    )