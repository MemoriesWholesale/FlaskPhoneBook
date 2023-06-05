"""empty message

Revision ID: 58b0cdd7095e
Revises: f12f41fb4f92
Create Date: 2023-06-05 00:40:49.026243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58b0cdd7095e'
down_revision = 'f12f41fb4f92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=25), nullable=False),
    sa.Column('last_name', sa.String(length=25), nullable=False),
    sa.Column('email', sa.String(length=75), nullable=True),
    sa.Column('address', sa.String(length=75), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.Numeric(precision=15), nullable=False),
    sa.Column('date_joined', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['user'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user')

    op.drop_table('user')
    # ### end Alembic commands ###
