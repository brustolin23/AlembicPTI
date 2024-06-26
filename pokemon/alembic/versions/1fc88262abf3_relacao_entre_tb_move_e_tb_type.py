"""Relacao entre tb_move e tb_type

Revision ID: 1fc88262abf3
Revises: 4364facd4a7f
Create Date: 2024-06-18 17:03:35.272653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1fc88262abf3'
down_revision: Union[str, None] = '4364facd4a7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_move', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_moveType', 'tb_type', ['move_type'], ['type_id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_move', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
