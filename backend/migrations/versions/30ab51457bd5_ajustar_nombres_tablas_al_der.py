"""ajustar nombres tablas al DER

Revision ID: 30ab51457bd5
Revises: ff0c6f8b4c09
Create Date: 2026-09-14 00:07:42.802067

"""

from alembic import op
import sqlalchemy as sa


revision = '30ab51457bd5'
down_revision = 'ff0c6f8b4c09'
branch_labels = None
depends_on = None



def upgrade():


    # ======================================================
    # TABLA grades
    #
    # Adaptación al DER:
    #
    # student_id      -> estudiante_id
    # evaluation_id   -> evaluacion_id
    # grade           -> nota
    #
    # ======================================================


    op.alter_column(
        "grades",
        "student_id",
        new_column_name="estudiante_id"
    )


    op.alter_column(
        "grades",
        "evaluation_id",
        new_column_name="evaluacion_id"
    )


    op.alter_column(
        "grades",
        "grade",
        new_column_name="nota",
        existing_type=sa.Numeric(5,2)
    )



    # ======================================================
    # TABLA attendance
    #
    # session_id     -> sesion_id
    # student_id     -> estudiante_id
    # status         -> estado
    #
    # ======================================================


    op.alter_column(
        "attendance",
        "session_id",
        new_column_name="sesion_id"
    )


    op.alter_column(
        "attendance",
        "student_id",
        new_column_name="estudiante_id"
    )


    op.alter_column(
        "attendance",
        "status",
        new_column_name="estado"
    )



    # ======================================================
    # TABLA incidents
    #
    # student_id          -> estudiante_id
    # teacher_course_id   -> asignacion_docente_id
    # type                -> tipo
    # description         -> descripcion
    # severity            -> gravedad
    # incident_date       -> fecha_incidente
    #
    # ======================================================


    op.alter_column(
        "incidents",
        "student_id",
        new_column_name="estudiante_id"
    )


    op.alter_column(
        "incidents",
        "teacher_course_id",
        new_column_name="asignacion_docente_id"
    )


    op.alter_column(
        "incidents",
        "type",
        new_column_name="tipo"
    )


    op.alter_column(
        "incidents",
        "description",
        new_column_name="descripcion"
    )


    op.alter_column(
        "incidents",
        "severity",
        new_column_name="gravedad"
    )


    op.alter_column(
        "incidents",
        "incident_date",
        new_column_name="fecha_incidente"
    )


    # Agregar relación con tema
    # para análisis IA por dificultad temática


    op.add_column(
        "incidents",
        sa.Column(
            "tema_id",
            sa.Integer(),
            nullable=True
        )
    )


    op.create_foreign_key(
        "fk_incidents_tema",
        "incidents",
        "topics",
        ["tema_id"],
        ["id"]
    )





def downgrade():


    # Eliminar FK tema

    op.drop_constraint(
        "fk_incidents_tema",
        "incidents",
        type_="foreignkey"
    )


    op.drop_column(
        "incidents",
        "tema_id"
    )



    # Restaurar nombres incidents


    op.alter_column(
        "incidents",
        "fecha_incidente",
        new_column_name="incident_date"
    )


    op.alter_column(
        "incidents",
        "gravedad",
        new_column_name="severity"
    )


    op.alter_column(
        "incidents",
        "descripcion",
        new_column_name="description"
    )


    op.alter_column(
        "incidents",
        "tipo",
        new_column_name="type"
    )


    op.alter_column(
        "incidents",
        "asignacion_docente_id",
        new_column_name="teacher_course_id"
    )


    op.alter_column(
        "incidents",
        "estudiante_id",
        new_column_name="student_id"
    )



    # Restaurar attendance


    op.alter_column(
        "attendance",
        "estado",
        new_column_name="status"
    )


    op.alter_column(
        "attendance",
        "estudiante_id",
        new_column_name="student_id"
    )


    op.alter_column(
        "attendance",
        "sesion_id",
        new_column_name="session_id"
    )



    # Restaurar grades


    op.alter_column(
        "grades",
        "nota",
        new_column_name="grade"
    )


    op.alter_column(
        "grades",
        "evaluacion_id",
        new_column_name="evaluation_id"
    )


    op.alter_column(
        "grades",
        "estudiante_id",
        new_column_name="student_id"
    )