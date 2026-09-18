"""corregir relaciones course assignments DER

Revision ID: 85ff4500a43c
Revises: 5f161452123c
Create Date: 2026-09-17 21:05:02.272090

"""
from alembic import op


revision = '85ff4500a43c'
down_revision = '5f161452123c'

branch_labels = None
depends_on = None



def upgrade():

    # =====================================
    # SESSIONS
    # =====================================

    with op.batch_alter_table("sessions") as batch_op:

        batch_op.alter_column(
            "teacher_course_id",
            new_column_name="course_assignment_id"
        )


    # =====================================
    # EVALUATIONS
    # =====================================

    with op.batch_alter_table("evaluations") as batch_op:

        batch_op.alter_column(
            "teacher_course_id",
            new_column_name="course_assignment_id"
        )


    # =====================================
    # INCIDENTS
    # =====================================

    with op.batch_alter_table("incidents") as batch_op:

        batch_op.alter_column(
            "asignacion_docente_id",
            new_column_name="course_assignment_id"
        )


    # =====================================
    # NUEVAS FK
    # =====================================

    op.create_foreign_key(
        "sessions_course_assignment_fk",
        "sessions",
        "course_assignments",
        ["course_assignment_id"],
        ["id"]
    )


    op.create_foreign_key(
        "evaluations_course_assignment_fk",
        "evaluations",
        "course_assignments",
        ["course_assignment_id"],
        ["id"]
    )


    op.create_foreign_key(
        "incidents_course_assignment_fk",
        "incidents",
        "course_assignments",
        ["course_assignment_id"],
        ["id"]
    )



def downgrade():

    pass