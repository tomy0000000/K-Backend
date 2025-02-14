"""Unify description fields

Revision ID: a72afc2909ca
Revises: 1c9946428c3f
Create Date: 2022-06-06 01:48:51.361085

"""

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "a72afc2909ca"
down_revision = "1c9946428c3f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "category", "description", existing_type=sa.VARCHAR(), nullable=True
    )
    op.alter_column("payment", "description", existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column(
        "payment_entry",
        "description",
        existing_type=sa.VARCHAR(),
        nullable=True,
    )
    op.add_column(
        "transaction",
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("transaction", "description")
    op.alter_column(
        "payment_entry",
        "description",
        existing_type=sa.VARCHAR(),
        nullable=False,
    )
    op.alter_column(
        "payment", "description", existing_type=sa.VARCHAR(), nullable=False
    )
    op.alter_column(
        "category", "description", existing_type=sa.VARCHAR(), nullable=False
    )
    # ### end Alembic commands ###
