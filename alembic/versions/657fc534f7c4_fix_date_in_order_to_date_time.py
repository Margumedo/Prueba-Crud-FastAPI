"""fix date in Order to date time

Revision ID: 657fc534f7c4
Revises: 7c3e67d87335
Create Date: 2023-12-03 11:50:19.003070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '657fc534f7c4'
down_revision = '7c3e67d87335'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('orders', 'date',
               existing_type=sa.VARCHAR(),
               type_=sa.DateTime(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('orders', 'date',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    # ### end Alembic commands ###
