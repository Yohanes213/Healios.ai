"""empty message

Revision ID: f97a9d85bebd
Revises: 0028a7b5a51a
Create Date: 2024-08-25 19:08:41.136690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f97a9d85bebd'
down_revision = '0028a7b5a51a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_bond')
    with op.batch_alter_table('bond', schema=None) as batch_op:
        batch_op.alter_column('tags',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)

    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment_id', sa.Integer(), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_column('comment_id')

    with op.batch_alter_table('bond', schema=None) as batch_op:
        batch_op.alter_column('tags',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)

    op.create_table('_alembic_tmp_bond',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('author', sa.VARCHAR(length=80), nullable=False),
    sa.Column('date_posted', sa.DATETIME(), nullable=True),
    sa.Column('title', sa.VARCHAR(length=80), nullable=True),
    sa.Column('tags', sa.VARCHAR(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
