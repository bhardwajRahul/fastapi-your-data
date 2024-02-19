"""Edit columns companies

Revision ID: 3813a9d96f3f
Revises: 398523055948
Create Date: 2024-01-25 12:28:08.608515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3813a9d96f3f'
down_revision = '398523055948'
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