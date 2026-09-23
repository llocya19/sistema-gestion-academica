from datetime import datetime

from app.extensions.database import db



from datetime import datetime

from app.extensions.database import db



# ==========================================================
# TABLA: persons
# ==========================================================

class Persona(db.Model):

    __tablename__ = "persons"


    id = db.Column(
        db.Integer,
        primary_key=True
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


    # --------------------------
    # Relaciones
    # --------------------------

    usuario = db.relationship(
        "Usuario",
        back_populates="persona",
        uselist=False
    )


    estudiante = db.relationship(
        "Estudiante",
        back_populates="persona",
        uselist=False
    )


    docente = db.relationship(
        "Docente",
        back_populates="persona",
        uselist=False
    )



# ==========================================================
# TABLA: students
# ==========================================================

class Estudiante(db.Model):

    __tablename__ = "students"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    student_code = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    person_id = db.Column(
        db.Integer,
        db.ForeignKey("persons.id"),
        nullable=False,
        unique=True
    )


    status = db.Column(
        db.Boolean,
        default=True
    )


    persona = db.relationship(
        "Persona",
        back_populates="estudiante"
    )



# ==========================================================
# TABLA: teachers
# ==========================================================

class Docente(db.Model):

    __tablename__ = "teachers"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    teacher_code = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    person_id = db.Column(
        db.Integer,
        db.ForeignKey("persons.id"),
        nullable=False,
        unique=True
    )


    status = db.Column(
        db.Boolean,
        default=True
    )


    persona = db.relationship(
        "Persona",
        back_populates="docente"
    )



# ==========================================================
# TABLA: courses
# ==========================================================

class Curso(db.Model):

    __tablename__ = "courses"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(150),
        nullable=False
    )


    code = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )


    description = db.Column(
        db.String(250)
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# ==========================================================
# TABLA: teacher_courses
# Relación docente - curso
# ==========================================================

class AsignacionDocente(db.Model):

    __tablename__ = "teacher_courses"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    teacher_id = db.Column(
        db.Integer,
        db.ForeignKey("teachers.id"),
        nullable=False
    )


    course_id = db.Column(
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



# ==========================================================
# TABLA: enrollments
# Matrícula estudiante - curso
# ==========================================================

class Matricula(db.Model):

    __tablename__ = "enrollments"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )


    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )


    academic_period = db.Column(
        db.String(50),
        nullable=False
    )


    status = db.Column(
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



# ==========================================================
# TABLA: sessions
# Sesiones de clase
# ==========================================================

class Sesion(db.Model):

    __tablename__ = "sessions"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    course_assignment_id = db.Column(
        db.Integer,
        db.ForeignKey("course_assignments.id"),
        nullable=False
    )


    title = db.Column(
        db.String(150),
        nullable=False
    )


    description = db.Column(
        db.Text
    )


    session_date = db.Column(
        db.Date
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    asignacion_curso = db.relationship(
        "AsignacionCurso",
        backref="sesiones"
    )

# ==========================================================
# TABLA: topics
# Temas desarrollados en sesión
# ==========================================================

class Tema(db.Model):

    __tablename__ = "topics"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    session_id = db.Column(
        db.Integer,
        db.ForeignKey("sessions.id"),
        nullable=False
    )


    name = db.Column(
        db.String(150),
        nullable=False
    )


    description = db.Column(
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
# Evaluaciones realizadas
# ==========================================================

class Evaluacion(db.Model):

    __tablename__ = "evaluations"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    course_assignment_id = db.Column(
        db.Integer,
        db.ForeignKey("course_assignments.id"),
        nullable=False
    )


    name = db.Column(
        db.String(150),
        nullable=False
    )


    evaluation_type = db.Column(
        db.String(50)
    )


    evaluation_date = db.Column(
        db.Date
    )


    evidence_url = db.Column(
        db.String(255)
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    asignacion_curso = db.relationship(
        "AsignacionCurso",
        backref="evaluaciones"
    )


# ==========================================================
# TABLA: grades
# Notas de estudiantes
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
# Asistencia
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
        db.String(50),
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
# Incidencias académicas
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


    course_assignment_id = db.Column(
        db.Integer,
        db.ForeignKey("course_assignments.id"),
        nullable=False
    )


    tipo = db.Column(
        db.String(100)
    )


    descripcion = db.Column(
        db.Text
    )


    gravedad = db.Column(
        db.String(50)
    )


    fecha_incidente = db.Column(
        db.Date
    )


    tema_id = db.Column(
        db.Integer,
        db.ForeignKey("topics.id")
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    estudiante = db.relationship(
        "Estudiante",
        backref="incidencias"
    )


    asignacion_curso = db.relationship(
        "AsignacionCurso",
        backref="incidencias"
    )


    tema = db.relationship(
        "Tema",
        backref="incidencias"
    )
# ==========================================================
# TABLA: grading_scales
# Escala de calificación
# ==========================================================

class GradingScale(db.Model):

    __tablename__ = "grading_scales"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(100),
        nullable=False
    )


    minimum_value = db.Column(
        db.Numeric(5,2),
        nullable=False
    )


    maximum_value = db.Column(
        db.Numeric(5,2),
        nullable=False
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )



# ==========================================================
# TABLA: academic_years
# Años académicos
# ==========================================================

class AnioAcademico(db.Model):

    __tablename__ = "academic_years"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    year = db.Column(
        db.Integer,
        nullable=False,
        unique=True
    )


    grading_scale_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "grading_scales.id"
        ),
        nullable=False
    )


    status = db.Column(
        db.Boolean,
        default=True
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    grading_scale = db.relationship(
        "GradingScale",
        backref="academic_years"
    )



# ==========================================================
# TABLA: academic_periods
# Periodos académicos
# ==========================================================

class PeriodoAcademico(db.Model):

    __tablename__ = "academic_periods"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    academic_year_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "academic_years.id"
        ),
        nullable=False
    )


    name = db.Column(
        db.String(100),
        nullable=False
    )


    start_date = db.Column(
        db.Date
    )


    end_date = db.Column(
        db.Date
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    academic_year = db.relationship(
        "AnioAcademico",
        backref="periodos"
    )



# ==========================================================
# TABLA: grade_levels
# Grados académicos
# ==========================================================

class Grado(db.Model):

    __tablename__ = "grade_levels"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(100),
        nullable=False
    )


    description = db.Column(
        db.String(200)
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )



# ==========================================================
# TABLA: sections
# Secciones académicas
# ==========================================================

class Seccion(db.Model):

    __tablename__ = "sections"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    grade_level_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "grade_levels.id"
        ),
        nullable=False
    )


    academic_year_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "academic_years.id"
        ),
        nullable=False
    )


    name = db.Column(
        db.String(50),
        nullable=False
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    grado = db.relationship(
        "Grado",
        backref="secciones"
    )


    anio_academico = db.relationship(
        "AnioAcademico",
        backref="secciones"
    )



# ==========================================================
# TABLA: student_enrollments
# Nueva matrícula según DER
# ==========================================================

class MatriculaEstudiante(db.Model):

    __tablename__ = "student_enrollments"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    student_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "students.id"
        ),
        nullable=False
    )


    academic_period_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "academic_periods.id"
        ),
        nullable=False
    )


    section_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "sections.id"
        ),
        nullable=False
    )


    status = db.Column(
        db.Boolean,
        default=True
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )



# ==========================================================
# TABLA: course_assignments
# Nueva asignación docente según DER
# ==========================================================
class AsignacionCurso(db.Model):

    __tablename__ = "course_assignments"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    teacher_id = db.Column(
        db.Integer,
        db.ForeignKey("teachers.id"),
        nullable=False
    )


    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )


    academic_period_id = db.Column(
        db.Integer,
        db.ForeignKey("academic_periods.id"),
        nullable=False
    )


    section_id = db.Column(
        db.Integer,
        db.ForeignKey("sections.id"),
        nullable=False
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    docente = db.relationship(
        "Docente"
    )


    curso = db.relationship(
        "Curso"
    )


    periodo = db.relationship(
        "PeriodoAcademico"
    )


    seccion = db.relationship(
        "Seccion"
    )
