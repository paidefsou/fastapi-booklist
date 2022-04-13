"""Create books table

Revision ID: c5f1d21bb1ef
Revises: 
Create Date: 2022-03-28 15:11:01.237320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5f1d21bb1ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('books', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('books')
    pass