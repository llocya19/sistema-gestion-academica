"""eliminar tablas antiguas teacher_courses y enrollments

Revision ID: 1617cb4f2588
Revises: 20c71b465ddc
Create Date: 2026-09-17 22:25:43.922472

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '1617cb4f2588'
down_revision = '20c71b465ddc'
branch_labels = None
depends_on = None


def upgrade():

    # Eliminar tabla antigua de asignaciones docente-curso
    op.drop_table(
        "teacher_courses"
    )


    # Eliminar tabla antigua de matrículas por curso
    op.drop_table(
        "enrollments"
    )


def downgrade():

    pass