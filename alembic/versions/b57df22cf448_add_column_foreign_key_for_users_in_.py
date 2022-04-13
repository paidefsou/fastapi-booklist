"""Add column foreign key for users in books table

Revision ID: b57df22cf448
Revises: a8d0d38007dd
Create Date: 2022-04-13 14:04:54.693289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b57df22cf448'
down_revision = 'a8d0d38007dd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('books', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('book_users_fk', source_table="books", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('book_users_fk', table_name="books")
    op.drop_column('posts', 'owner_id')
    pass