"""Inclusao da tabela tb_canLearn

Revision ID: db0e9c6afa6b
Revises: 3683adbbe528
Create Date: 2024-06-19 15:37:13.813778

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db0e9c6afa6b'
down_revision: Union[str, None] = '3683adbbe528'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_canLearn',
    sa.Column('canL_id', sa.Integer(), nullable=False),
    sa.Column('canL_pokemon', sa.Integer(), nullable=True),
    sa.Column('canL_move', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('canL_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_canLearn')
    # ### end Alembic commands ###
