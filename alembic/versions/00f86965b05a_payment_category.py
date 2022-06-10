"""Payment Category

Revision ID: 00f86965b05a
Revises: 5a4906bfb3bd
Create Date: 2022-06-10 16:08:08.050576

"""
import warnings

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "00f86965b05a"
down_revision = "5a4906bfb3bd"
branch_labels = None
depends_on = None

payment_category_enum = sa.Enum("Expense", "Income", "Transfer", name="paymentcategory")


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    payment_category_enum.create(op.get_bind(), checkfirst=True)
    op.add_column(
        "payment", sa.Column("category", payment_category_enum, nullable=True)
    )
    warnings.warn(
        "Payment category is Non-nullable in next revision, please set it manually for all payments"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("payment", "category")
    payment_category_enum.drop(op.get_bind(), checkfirst=True)
    # ### end Alembic commands ###
