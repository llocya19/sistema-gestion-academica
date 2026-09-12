from datetime import datetime

from app.extensions.database import db


# ==========================================================
# TABLA: academic_indicators
#
# Guarda resultados históricos del análisis académico.
#
# Estos datos serán utilizados posteriormente
# por el módulo de IA.
#
# ==========================================================


class AcademicIndicator(db.Model):

    __tablename__ = "academic_indicators"


    # Identificador
    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # Estudiante analizado
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )


    # Promedio académico calculado
    average_grade = db.Column(
        db.Numeric(5,2),
        nullable=False
    )


    # Porcentaje de asistencia
    attendance_percentage = db.Column(
        db.Numeric(5,2),
        nullable=False
    )


    # Número de incidencias
    incidents_count = db.Column(
        db.Integer,
        nullable=False
    )


    # Riesgo:
    # BAJO
    # MEDIO
    # ALTO

    risk_level = db.Column(
        db.String(20),
        nullable=False
    )


    # Fecha de generación

    generated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )