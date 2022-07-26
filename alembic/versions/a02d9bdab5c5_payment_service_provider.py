"""Payment Service Provider

Revision ID: a02d9bdab5c5
Revises: e4e019712d5d
Create Date: 2022-06-30 08:54:49.027101

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "a02d9bdab5c5"
down_revision = "e4e019712d5d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "payment_service_providers",
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("payment_service_providers")
    # ### end Alembic commands ###
