"""add price column

Revision ID: 8ca3dd2e4424
Revises: 17f4fa772bb8
Create Date: 2022-06-19 15:58:31.129899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ca3dd2e4424'
down_revision = '17f4fa772bb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Product', sa.Column('price', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Product', 'price')
    # ### end Alembic commands ###
