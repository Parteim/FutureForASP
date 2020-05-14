"""empty message

Revision ID: fd219ad38102
Revises: dc4fff7d0fe4
Create Date: 2020-05-14 14:56:40.192069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd219ad38102'
down_revision = 'dc4fff7d0fe4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('text', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'text')
    # ### end Alembic commands ###
