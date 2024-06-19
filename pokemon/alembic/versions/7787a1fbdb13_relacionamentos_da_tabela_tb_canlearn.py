"""Relacionamentos da tabela tb_canLearn

Revision ID: 7787a1fbdb13
Revises: db0e9c6afa6b
Create Date: 2024-06-19 15:37:48.625027

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7787a1fbdb13'
down_revision: Union[str, None] = 'db0e9c6afa6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_canLearn', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_canLPokemon', 'tb_pokemon', ['canL_pokemon'], ['poke_registerDex'])
        batch_op.create_foreign_key('fk_canLMove', 'tb_move', ['canL_move'], ['move_id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_canLearn', schema=None) as batch_op:
        batch_op.drop_constraint('fk_canLPokemon', type_='foreignkey')
        batch_op.drop_constraint('fk_canLMove', type_='foreignkey')

    # ### end Alembic commands ###