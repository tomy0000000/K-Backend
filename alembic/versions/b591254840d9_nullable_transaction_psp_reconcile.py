"""Test

Revision ID: b591254840d9
Revises: 90e77fb7e8ff
Create Date: 2025-01-20 16:15:56.940067

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b591254840d9"
down_revision = "90e77fb7e8ff"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "transaction",
        "psp_reconcile",
        existing_type=sa.BOOLEAN(),
        nullable=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "transaction",
        "psp_reconcile",
        existing_type=sa.BOOLEAN(),
        nullable=False,
    )
    # ### end Alembic commands ###
