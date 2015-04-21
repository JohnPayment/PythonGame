#!/usr/bin/python
from enum import Enum

class AutoNumber(Enum):
	def __new__(cls):
		value = len(cls.__members__) + 1
		obj = object.__new__(cls)
		obj._value_ = value
		return obj

class Effects(AutoNumber):
	NoEffect = ()
	# Target fails next attack if slower
	Flinch = ()
	# Cannot act. Chance to wake up each turn, with chance increases after recieving damage
	Sleep = ()
	# Chance to hurt self. Chance to be cured each turn with chance increasing after taking damage
	Confusion = ()
	# Takes damage based upon how much damage is dealt
	Recoil = ()
	# Takes damage based upon a percentage of your total HP
	PercentRecoil = ()

class Types(AutoNumber):
	Normal = ()
	Fire = ()
	Water = ()
	Wind = ()
	Earth = ()

class Attributes(AutoNumber):
	NoAttr = ()
	HP = ()
	STR = ()
	MSTR = ()
	DEF = ()
	MDEF = ()
	SPD = ()
	#Normally Static
	EVA = ()
	ACC = ()

