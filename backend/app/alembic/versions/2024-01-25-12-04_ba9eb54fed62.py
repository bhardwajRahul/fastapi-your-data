"""add column test

Revision ID: ba9eb54fed62
Revises: 8a3e4b8f3672
Create Date: 2024-01-25 12:04:42.863847

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel # added


# revision identifiers, used by Alembic.
revision = 'ba9eb54fed62'
down_revision = '8a3e4b8f3672'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm") 
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('companies', sa.Column('founded', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('companies', 'founded')
    # ### end Alembic commands ###
