"""Switch report.data to JSONB

Revision ID: 51215ee91d24
Revises: 97ab43794f68
Create Date: 2025-05-20 09:25:24.727243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51215ee91d24'
down_revision = '97ab43794f68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('document', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path', sa.String(), nullable=True))

    with op.batch_alter_table('report', schema=None) as batch_op:
        batch_op.drop_index('idx_report_data_jsonpath', postgresql_using='gin')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('report', schema=None) as batch_op:
        batch_op.create_index('idx_report_data_jsonpath', ['data'], unique=False, postgresql_using='gin')

    with op.batch_alter_table('document', schema=None) as batch_op:
        batch_op.drop_column('image_path')

    # ### end Alembic commands ###
