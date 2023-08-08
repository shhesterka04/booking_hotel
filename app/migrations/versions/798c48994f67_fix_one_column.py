"""fix one column

Revision ID: 798c48994f67
Revises: dc2e9f794253
Create Date: 2023-08-03 18:25:04.049407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '798c48994f67'
down_revision = 'dc2e9f794253'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('hotels', 'image_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('hotels', 'image_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###