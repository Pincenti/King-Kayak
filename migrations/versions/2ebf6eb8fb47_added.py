"""added

Revision ID: 2ebf6eb8fb47
Revises: 41a760b0a930
Create Date: 2021-06-02 21:46:28.386140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ebf6eb8fb47'
down_revision = '41a760b0a930'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('created_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'created_on')
    # ### end Alembic commands ###
