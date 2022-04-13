"""Add publication year column in books table

Revision ID: bf0b509f9e24
Revises: c5f1d21bb1ef
Create Date: 2022-03-28 15:20:17.234224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf0b509f9e24'
down_revision = 'c5f1d21bb1ef'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('books', sa.Column('publication_year', sa.Integer(), nullable=False))
    pass


def downgrade():
    op.drop_column('books', 'publication_year')
    pass