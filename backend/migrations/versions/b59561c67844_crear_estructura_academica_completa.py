"""
crear estructura academica completa

Revision ID: b59561c67844
Revises: c51de55f0d95
Create Date: 2026-09-16 22:00:28.506999

"""

from alembic import op
import sqlalchemy as sa


revision = 'b59561c67844'
down_revision = 'c51de55f0d95'
branch_labels = None
depends_on = None



def upgrade():


    # =====================================================
    # TABLA: grading_scales
    # =====================================================

    op.create_table(

        'grading_scales',

        sa.Column(
            'id',
            sa.Integer(),
            primary_key=True
        ),

        sa.Column(
            'name',
            sa.String(100),
            nullable=False
        ),

        sa.Column(
            'minimum_value',
            sa.Numeric(5,2),
            nullable=False
        ),

        sa.Column(
            'maximum_value',
            sa.Numeric(5,2),
            nullable=False
        ),

        sa.Column(
            'created_at',
            sa.DateTime(),
            server_default=sa.func.now()
        )

    )



    # =====================================================
    # TABLA: academic_years
    # =====================================================

    op.create_table(

        'academic_years',

        sa.Column(
            'id',
            sa.Integer(),
            primary_key=True
        ),

        sa.Column(
            'year',
            sa.Integer(),
            nullable=False,
            unique=True
        ),

        sa.Column(
            'grading_scale_id',
            sa.Integer(),
            sa.ForeignKey(
                'grading_scales.id'
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
    # TABLA: academic_periods
    # =====================================================

    op.create_table(

        'academic_periods',

        sa.Column(
            'id',
            sa.Integer(),
            primary_key=True
        ),

        sa.Column(
            'academic_year_id',
            sa.Integer(),
            sa.ForeignKey(
                'academic_years.id'
            ),
            nullable=False
        ),

        sa.Column(
            'name',
            sa.String(100),
            nullable=False
        ),

        sa.Column(
            'start_date',
            sa.Date()
        ),

        sa.Column(
            'end_date',
            sa.Date()
        ),

        sa.Column(
            'created_at',
            sa.DateTime(),
            server_default=sa.func.now()
        )

    )



    # =====================================================
    # TABLA: grade_levels
    # =====================================================

    op.create_table(

        'grade_levels',

        sa.Column(
            'id',
            sa.Integer(),
            primary_key=True
        ),

        sa.Column(
            'name',
            sa.String(100),
            nullable=False
        ),

        sa.Column(
            'description',
            sa.String(200)
        ),

        sa.Column(
            'created_at',
            sa.DateTime(),
            server_default=sa.func.now()
        )

    )



    # =====================================================
    # TABLA: sections
    # =====================================================

    op.create_table(

        'sections',

        sa.Column(
            'id',
            sa.Integer(),
            primary_key=True
        ),

        sa.Column(
            'grade_level_id',
            sa.Integer(),
            sa.ForeignKey(
                'grade_levels.id'
            ),
            nullable=False
        ),

        sa.Column(
            'academic_year_id',
            sa.Integer(),
            sa.ForeignKey(
                'academic_years.id'
            ),
            nullable=False
        ),

        sa.Column(
            'name',
            sa.String(50),
            nullable=False
        ),

        sa.Column(
            'created_at',
            sa.DateTime(),
            server_default=sa.func.now()
        )

    )





def downgrade():


    op.drop_table('sections')

    op.drop_table('grade_levels')

    op.drop_table('academic_periods')

    op.drop_table('academic_years')

    op.drop_table('grading_scales')