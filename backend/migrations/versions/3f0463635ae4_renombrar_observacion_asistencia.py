"""renombrar observacion asistencia

Revision ID: 3f0463635ae4
Revises: 30ab51457bd5
Create Date: 2026-09-14

"""

from alembic import op


revision = "3f0463635ae4"
down_revision = "30ab51457bd5"

branch_labels = None
depends_on = None



def upgrade():

    op.alter_column(
        "attendance",
        "observation",
        new_column_name="observacion"
    )



def downgrade():

    op.alter_column(
        "attendance",
        "observacion",
        new_column_name="observation"
    )