"""add field active to Store model

Revision ID: ce75e1e65715
Revises: fbd49676dc62
Create Date: 2020-07-21 07:47:19.706495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce75e1e65715'
down_revision = 'fbd49676dc62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'active')
    # ### end Alembic commands ###