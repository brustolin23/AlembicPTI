"""Relacionamentos da tabela tb_learnByLevelUp

Revision ID: 3683adbbe528
Revises: 84f1aa725184
Create Date: 2024-06-19 15:31:18.795967

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3683adbbe528'
down_revision: Union[str, None] = '84f1aa725184'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_learnByLevelUp', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_learnLvPokemon', 'tb_pokemon', ['LBLU_pokemon'], ['poke_registerDex'])
        batch_op.create_foreign_key('fk_learnLvMove', 'tb_move', ['LBLU_move'], ['move_id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_learnByLevelUp', schema=None) as batch_op:
        batch_op.drop_constraint('fk_learnLvPokemon', type_='foreignkey')
        batch_op.drop_constraint('fk_learnLvMove', type_='foreignkey')

    # ### end Alembic commands ###