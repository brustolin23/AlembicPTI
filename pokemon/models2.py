from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TbPokemon(Base):
    __tablename__ = 'tb_pokemon'

    poke_registerDex = Column(Integer, primary_key=True)
    poke_name = Column(String(20), nullable=False)
    pokedex_entry = Column(String(500), nullable=False)
    poke_height = Column(Float, nullable=False)
    poke_weight = Column(Float, nullable=False)
    poke_picture = Column(String(10), nullable=False)
