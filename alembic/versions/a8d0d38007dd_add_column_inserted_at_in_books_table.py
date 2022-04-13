"""Add column inserted at in books table

Revision ID: a8d0d38007dd
Revises: 3d0f3b5c022d
Create Date: 2022-04-13 13:21:31.035067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8d0d38007dd'
down_revision = '3d0f3b5c022d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('books', sa.Column(
        'inserted_at_database', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('books', 'inserted_at_database')
    pass