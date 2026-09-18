"""
ajustar matricula y asignaciones segun DER

Revision ID: 5f161452123c
Revises: b59561c67844

"""

from alembic import op
import sqlalchemy as sa


revision = '5f161452123c'
down_revision = 'b59561c67844'
branch_labels = None
depends_on = None



def upgrade():


    # =====================================================
    # TABLA: student_enrollments
    # Matrícula real según DER
    # =====================================================

    op.create_table(

        'student_enrollments',

        sa.Column(
            'id',
            sa.Integer(),
            primary_key=True
        ),


        sa.Column(
            'student_id',
            sa.Integer(),
            sa.ForeignKey(
                'students.id'
            ),
            nullable=False
        ),


        sa.Column(
            'academic_period_id',
            sa.Integer(),
            sa.ForeignKey(
                'academic_periods.id'
            ),
            nullable=False
        ),


        sa.Column(
            'section_id',
            sa.Integer(),
            sa.ForeignKey(
                'sections.id'
            ),
            nullable=False
        ),


        sa.Column(
            'status',
            sa.Boolean(),
            default=True
        ),


        sa.Column(
            'created_at',
            sa.DateTime(),
            server_default=sa.func.now()
        )

    )



    # =====================================================
    # TABLA: course_assignments
    # Asignación docente según DER
    # =====================================================

    op.create_table(

        'course_assignments',

        sa.Column(
            'id',
            sa.Integer(),
            primary_key=True
        ),


        sa.Column(
            'teacher_id',
            sa.Integer(),
            sa.ForeignKey(
                'teachers.id'
            ),
            nullable=False
        ),


        sa.Column(
            'course_id',
            sa.Integer(),
            sa.ForeignKey(
                'courses.id'
            ),
            nullable=False
        ),


        sa.Column(
            'academic_period_id',
            sa.Integer(),
            sa.ForeignKey(
                'academic_periods.id'
            ),
            nullable=False
        ),


        sa.Column(
            'section_id',
            sa.Integer(),
            sa.ForeignKey(
                'sections.id'
            ),
            nullable=False
        ),


        sa.Column(
            'created_at',
            sa.DateTime(),
            server_default=sa.func.now()
        )

    )





def downgrade():


    op.drop_table(
        'course_assignments'
    )


    op.drop_table(
        'student_enrollments'
    )