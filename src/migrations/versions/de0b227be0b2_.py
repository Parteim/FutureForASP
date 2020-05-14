"""empty message

Revision ID: de0b227be0b2
Revises: 7c6adbb9c64a
Create Date: 2020-05-14 11:55:11.408754

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'de0b227be0b2'
down_revision = '7c6adbb9c64a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recip_image')
    op.add_column('recipes', sa.Column('image', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipes', 'image')
    op.create_table('recip_image',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('url', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
