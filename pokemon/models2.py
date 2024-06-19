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
    poke_baseStats = Column(ForeignKey("tb_status.stat_id"))
    poke_primaryAbility = Column(ForeignKey("tb_ability.ablt_id"))
    poke_secondaryAbility = Column(ForeignKey("tb_ability.ablt_id"))
    poke_hiddenAbility = Column(ForeignKey("tb_ability.ablt_id"))
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
    tyAd_attackType = Column(ForeignKey("tb_type.type_id"))
    tyAd_defenseType = Column(ForeignKey("tb_type.type_id"))
    tyAd_typeAdvantage = Column(ForeignKey("tb_combatAdvantage.cmAd_id"))

class TbStats(Base):
    __tablename__ = 'tb_status'

    stat_id = Column(Integer, primary_key=True)
    stat_hp = Column(Integer, nullable=False)
    stat_attack = Column(Integer, nullable=False)
    stat_defense = Column(Integer, nullable=False)
    stat_spAttack = Column(Integer, nullable=False)
    stat_spDefense = Column(Integer, nullable=False)
    stat_speed = Column(Integer, nullable=False)


class TbAbility(Base):
    __tablename__ = 'tb_ability'

    ablt_id = Column(Integer, primary_key=True)
    ablt_name = Column(String(30), nullable=False)
    ablt_effect = Column(String(100), nullable=False)

class TbMove(Base):
    __tablename__ = 'tb_move'

    move_id = Column(Integer, primary_key=True)
    move_name = Column(String(20), nullable=False)
    move_type = Column(ForeignKey("tb_type.type_id"))
    move_category = Column(Integer)
    move_power = Column(Integer)
    move_accuracy = Column(Integer)
    move_basePP = Column(Integer)
    move_description = Column(String(100), nullable=False)
    move_effect = Column(String(100), nullable=False)

class TbLearnByLevelUp(Base):
    __tablename__ = 'tb_learnByLevelUp'

    LBLU_id = Column(Integer, primary_key=True)
    LBLU_pokemon = Column(ForeignKey("tb_pokemon.poke_registerDex"))
    LBLU_move = Column(ForeignKey("tb_move.move_id"))
    LBLU_level = Column(Integer)

class TbCanLearn(Base):
    __tablename__ = 'tb_canLearn'

    canL_id = Column(Integer, primary_key=True)
    canL_pokemon = Column(ForeignKey("tb_pokemon.poke_registerDex"))
    canL_move = Column(ForeignKey("tb_move.move_id"))

