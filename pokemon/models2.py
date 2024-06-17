from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TbPokemon(Base):
    __tablename__ = 'tb_pokemon'

    poke_registerDex = Column(Integer, primary_key=True)
    poke_name = Column(String(20), nullable=False)
    pokedex_entry = Column(String(500), nullable=False)
    poke_primaryType = Column(ForeignKey("tb_type.type_id"))
    poke_secondaryType = Column(ForeignKey("tb_type.type_id"))
    poke_height = Column(Float, nullable=False)
    poke_weight = Column(Float, nullable=False)
    poke_picture = Column(String(10), nullable=False)

class TbType(Base):
    __tablename__ = 'tb_type'

    type_id = Column(Integer, primary_key=True)
    type_name = Column(String(20), nullable=False)
    type_picture = Column(String(10), nullable=False)

class TbCombatAdvantage(Base):
    __tablename__ = 'tb_combatAdvantage'

    cmAd_id = Column(Integer, primary_key=True)
    cmAd_name = Column(String(20), nullable=False)
    cmAd_multiplier = Column(Float, nullable=False)

class TbTypeAdvantage(Base):
    __tablename__ = 'tb_typeAdvantage'

    tyAd_id = Column(Integer, primary_key=True)
    tyAd_attackType = Column(Integer)
    tyAd_defenseType = Column(Integer)
    tyAd_typeAdvantage = Column(Integer)
