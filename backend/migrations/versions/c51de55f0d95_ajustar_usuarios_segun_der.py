"""ajustar usuarios segun DER

Revision ID: c51de55f0d95
Revises: e9a123c4d896
Create Date: 2026-09-16 21:04:23.965101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c51de55f0d95'
down_revision = 'e9a123c4d896'
branch_labels = None
depends_on = None


def upgrade():

    # Eliminar datos personales duplicados de usuario
    op.drop_column(
        "users",
        "first_name"
    )

    op.drop_column(
        "users",
        "last_name"
    )


    # Agregar campos de control de acceso

    op.add_column(
        "users",
        sa.Column(
            "last_login",
            sa.DateTime(),
            nullable=True
        )
    )


    op.add_column(
        "users",
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=True
        )
    )



def downgrade():

    # Eliminar campos nuevos

    op.drop_column(
        "users",
        "last_login"
    )


    op.drop_column(
        "users",
        "updated_at"
    )


    # Restaurar campos antiguos

    op.add_column(
        "users",
        sa.Column(
            "first_name",
            sa.String(100),
            nullable=True
        )
    )


    op.add_column(
        "users",
        sa.Column(
            "last_name",
            sa.String(100),
            nullable=True
        )
    )