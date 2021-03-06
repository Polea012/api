"""empty message

Revision ID: f4d09b3091ce
Revises: 5e9efdf64425
Create Date: 2019-10-23 01:29:40.156085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4d09b3091ce'
down_revision = '5e9efdf64425'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('found', sa.Boolean(), nullable=True))
    op.add_column('person', sa.Column('found_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'found_date')
    op.drop_column('person', 'found')
    # ### end Alembic commands ###
