"""Account balance

Revision ID: b57d9713593a
Revises: a72afc2909ca
Create Date: 2022-06-06 02:54:41.128753

"""
import warnings

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b57d9713593a"
down_revision = "a72afc2909ca"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("account", sa.Column("balance", sa.Numeric(), nullable=True))
    warnings.warn(
        "Account balance is Non-nullable in next revision, please set it manually for all accounts"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("account", "balance")
    # ### end Alembic commands ###
