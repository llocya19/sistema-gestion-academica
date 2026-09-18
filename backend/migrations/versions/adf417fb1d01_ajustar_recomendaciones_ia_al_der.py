"""ajustar recomendaciones IA al DER

Revision ID: adf417fb1d01
Revises: b1fd6020230f
Create Date: 2026-09-14 00:24:19.744097

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = 'adf417fb1d01'
down_revision = 'b1fd6020230f'
branch_labels = None
depends_on = None
def upgrade():

    # ======================================================
    # TABLA: ai_recommendations
    #
    # Ajuste según DER
    #
    # student_id       -> estudiante_id
    # category         -> categoria
    # message          -> mensaje
    # created_at       -> fecha_generacion
    #
    # ======================================================


    op.alter_column(
        "ai_recommendations",
        "student_id",
        new_column_name="estudiante_id"
    )


    op.alter_column(
        "ai_recommendations",
        "category",
        new_column_name="categoria"
    )


    op.alter_column(
        "ai_recommendations",
        "message",
        new_column_name="mensaje"
    )


    op.alter_column(
        "ai_recommendations",
        "created_at",
        new_column_name="fecha_generacion"
    )



def downgrade():

    op.alter_column(
        "ai_recommendations",
        "fecha_generacion",
        new_column_name="created_at"
    )


    op.alter_column(
        "ai_recommendations",
        "mensaje",
        new_column_name="message"
    )


    op.alter_column(
        "ai_recommendations",
        "categoria",
        new_column_name="category"
    )


    op.alter_column(
        "ai_recommendations",
        "estudiante_id",
        new_column_name="student_id"
    )