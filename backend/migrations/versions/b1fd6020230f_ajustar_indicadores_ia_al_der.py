"""ajustar indicadores IA al DER

Revision ID: b1fd6020230f
Revises: 3f0463635ae4
Create Date: 2026-09-14 00:21:39.844766

"""

from alembic import op
import sqlalchemy as sa


revision = 'b1fd6020230f'
down_revision = '3f0463635ae4'
branch_labels = None
depends_on = None



def upgrade():


    # ======================================================
    # TABLA academic_indicators
    #
    # Ajuste al DER
    #
    # student_id              -> estudiante_id
    # average_grade           -> promedio
    # attendance_percentage   -> porcentaje_asistencia
    # incidents_count         -> cantidad_incidencias
    # risk_level              -> nivel_riesgo
    # generated_at            -> fecha_generacion
    #
    # ======================================================


    op.alter_column(
        "academic_indicators",
        "student_id",
        new_column_name="estudiante_id"
    )


    op.alter_column(
        "academic_indicators",
        "average_grade",
        new_column_name="promedio",
        existing_type=sa.Numeric(5,2)
    )


    op.alter_column(
        "academic_indicators",
        "attendance_percentage",
        new_column_name="porcentaje_asistencia",
        existing_type=sa.Numeric(5,2)
    )


    op.alter_column(
        "academic_indicators",
        "incidents_count",
        new_column_name="cantidad_incidencias"
    )


    op.alter_column(
        "academic_indicators",
        "risk_level",
        new_column_name="nivel_riesgo"
    )


    op.alter_column(
        "academic_indicators",
        "generated_at",
        new_column_name="fecha_generacion"
    )



def downgrade():


    op.alter_column(
        "academic_indicators",
        "fecha_generacion",
        new_column_name="generated_at"
    )


    op.alter_column(
        "academic_indicators",
        "nivel_riesgo",
        new_column_name="risk_level"
    )


    op.alter_column(
        "academic_indicators",
        "cantidad_incidencias",
        new_column_name="incidents_count"
    )


    op.alter_column(
        "academic_indicators",
        "porcentaje_asistencia",
        new_column_name="attendance_percentage",
        existing_type=sa.Numeric(5,2)
    )


    op.alter_column(
        "academic_indicators",
        "promedio",
        new_column_name="average_grade",
        existing_type=sa.Numeric(5,2)
    )


    op.alter_column(
        "academic_indicators",
        "estudiante_id",
        new_column_name="student_id"
    )