from datetime import datetime

from app.extensions.database import db



# ==========================================================
# TABLA: academic_indicators
#
# Guarda el historial de análisis académico generado
# por el módulo IA.
#
# Relación:
#
# estudiante 1 ----- N análisis IA
#
# ==========================================================


class AnalisisIA(db.Model):

    __tablename__ = "academic_indicators"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    estudiante_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )


    promedio = db.Column(
        db.Numeric(5,2),
        nullable=False
    )


    porcentaje_asistencia = db.Column(
        db.Numeric(5,2),
        nullable=False
    )


    cantidad_incidencias = db.Column(
        db.Integer,
        nullable=False
    )


    nivel_riesgo = db.Column(
        db.String(20),
        nullable=False
    )


    fecha_generacion = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    estudiante = db.relationship(
        "Estudiante",
        backref="analisis_ia"
    )



# ==========================================================
# TABLA: ai_recommendations
#
# Guarda recomendaciones generadas por IA.
#
# Relación:
#
# estudiante 1 ----- N recomendaciones
#
# ==========================================================


class RecomendacionIA(db.Model):

    __tablename__ = "ai_recommendations"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    estudiante_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )


    categoria = db.Column(
        db.String(50),
        nullable=False
    )


    mensaje = db.Column(
        db.Text,
        nullable=False
    )


    fecha_generacion = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    estudiante = db.relationship(
        "Estudiante",
        backref="recomendaciones_ia"
    )