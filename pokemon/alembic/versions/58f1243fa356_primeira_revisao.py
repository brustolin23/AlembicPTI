"""primeira revisao

Revision ID: 58f1243fa356
Revises: 
Create Date: 2024-06-13 15:18:56.758251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58f1243fa356'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tb_pokemon',
        sa.Column('poke_registerDex', sa.Integer, primary_key=True),
        sa.Column('poke_name', sa.String(length=20), nullable=False),
        sa.Column('pokedex_entry', sa.String(length=500), nullable=False),
        sa.Column('poke_height', sa.Float, nullable=False),
        sa.Column('poke_weight', sa.Float, nullable=False),
        sa.Column('poke_picture', sa.String(length=10), nullable=False, default='empty.png')
    )


def downgrade() -> None:
    op.drop_table('tb_pokemon')
