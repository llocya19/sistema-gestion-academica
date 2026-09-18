"""corregir relacion persona usuario

Revision ID: e9a123c4d896
Revises: adf417fb1d01
Create Date: 2026-09-16 20:54:40.720431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9a123c4d896'
down_revision = 'adf417fb1d01'
branch_labels = None
depends_on = None


def upgrade():

    # 1. Crear persona_id temporal en users
    op.add_column(
        "users",
        sa.Column(
            "persona_id",
            sa.Integer(),
            nullable=True
        )
    )


    # 2. Relacionar usuarios existentes con personas existentes
    op.execute(
        """
        UPDATE users
        SET persona_id = persons.id
        FROM persons
        WHERE persons.user_id = users.id
        """
    )


    # 3. Hacer obligatorio persona_id
    op.alter_column(
        "users",
        "persona_id",
        nullable=False
    )


    # 4. Crear FK
    op.create_foreign_key(
        "fk_users_persona",
        "users",
        "persons",
        ["persona_id"],
        ["id"]
    )


    # 5. Renombrar campos de persona

    op.alter_column(
        "persons",
        "first_name",
        new_column_name="nombres"
    )

    op.alter_column(
        "persons",
        "last_name",
        new_column_name="apellidos"
    )

    op.alter_column(
        "persons",
        "phone",
        new_column_name="telefono"
    )

    op.alter_column(
        "persons",
        "address",
        new_column_name="direccion"
    )


    # 6. Eliminar relación antigua

    op.drop_constraint(
        "persons_user_id_fkey",
        "persons",
        type_="foreignkey"
    )

    op.drop_column(
        "persons",
        "user_id"
    )

def downgrade():

    op.add_column(
        "persons",
        sa.Column(
            "user_id",
            sa.Integer(),
            nullable=True
        )
    )


    op.execute(
        """
        UPDATE persons
        SET user_id = users.id
        FROM users
        WHERE users.persona_id = persons.id
        """
    )


    op.drop_constraint(
        "fk_users_persona",
        "users",
        type_="foreignkey"
    )


    op.drop_column(
        "users",
        "persona_id"
    )


    op.alter_column(
        "persons",
        "nombres",
        new_column_name="first_name"
    )

    op.alter_column(
        "persons",
        "apellidos",
        new_column_name="last_name"
    )

    op.alter_column(
        "persons",
        "telefono",
        new_column_name="phone"
    )

    op.alter_column(
        "persons",
        "direccion",
        new_column_name="address"
    )
