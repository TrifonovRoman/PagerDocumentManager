"""Alter text_content to citext

Revision ID: 1b7b5c526d72
Revises: b3b7b8bb534a
Create Date: 2025-05-12 00:32:02.343658

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1b7b5c526d72'
down_revision = 'b3b7b8bb534a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('report', schema=None) as batch_op:
        batch_op.alter_column('text_content',
               existing_type=sa.TEXT(),
               type_=postgresql.CITEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('report', schema=None) as batch_op:
        batch_op.alter_column('text_content',
               existing_type=postgresql.CITEXT(),
               type_=sa.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###
