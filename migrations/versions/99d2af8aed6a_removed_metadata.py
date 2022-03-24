"""Removed Metadata

Revision ID: 99d2af8aed6a
Revises: c0a81373d996
Create Date: 2022-03-24 16:01:03.420719

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '99d2af8aed6a'
down_revision = 'c0a81373d996'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('doctor', 'meta_data')
    op.drop_column('hospital', 'meta_data')
    op.drop_column('patient', 'meta_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient', sa.Column('meta_data', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.add_column('hospital', sa.Column('meta_data', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.add_column('doctor', sa.Column('meta_data', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
