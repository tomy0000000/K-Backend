"""Revise Invoice Detail

Revision ID: c48d26a61bef
Revises: 7c2873a67659
Create Date: 2022-06-19 00:32:08.195611

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c48d26a61bef"
down_revision = "7c2873a67659"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("invoice_detail", "id")
    op.create_primary_key(
        "invoice_detail_pkey", "invoice_detail", ["invoice_number", "row_number"]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("invoice_detail_pkey", "invoice_detail", type_="primary")
    op.add_column(
        "invoice_detail",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
    )
    op.create_primary_key("invoice_detail_pkey", "invoice_detail", ["id"])
    # ### end Alembic commands ###
