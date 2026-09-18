"""eliminar fk antiguas teacher_courses

Revision ID: 20c71b465ddc
Revises: 85ff4500a43c
Create Date: 2026-09-17

"""

from alembic import op


revision = "20c71b465ddc"
down_revision = "85ff4500a43c"

branch_labels = None
depends_on = None



def upgrade():


    # =====================================
    # ELIMINAR FK ANTIGUAS
    # teacher_courses
    # =====================================


    op.drop_constraint(
        "sessions_teacher_course_id_fkey",
        "sessions",
        type_="foreignkey"
    )


    op.drop_constraint(
        "evaluations_teacher_course_id_fkey",
        "evaluations",
        type_="foreignkey"
    )


    op.drop_constraint(
        "incidents_teacher_course_id_fkey",
        "incidents",
        type_="foreignkey"
    )



def downgrade():

    pass