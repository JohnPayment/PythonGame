#!/usr/bin/python
from Standards import AutoNumber, Effects, Types, Attributes

# HP (Hit Points)
# STR (Strength)
# DEF (Defense)
# MSTR (Magic Strength)
# MDEF (Magic Defense)
# SPD (Speed)
class Attributes():
	#Attributes
	def __init__(self, HP, STR, DEF, MSTR, MDEF, SPD):
		self.HP = HP
		self.STR = STR
		self.DEF = DEF
		self.MSTR = MSTR
		self.MDEF = MDEF
		self.SPD = SPD

# attr (base values)
#	HP
#	STR
#	DEF
#	MSTR
#	MDEF
#	SPD
# attack[level] (array on which each index references the level on which if can be accessed)
#	attack1
#	...
#	attackN
# typeOne (Mon type #1)
# typeTwo (Mon type #2)
class BasicMon():
	def __init__(self, attrs, typeOne, typeTwo):
		self.attr = attrs
		self.typeOne = typeOne
		self.typeTwo = typeTwo

	def addAttack(self, attack, level):
		self.attack[level] = attack

# original (BasicMon Template)
# 	attr
#		HP
#		STR
#		DEF
#		MSTR
#		MDEF
#		SPD
#	attack[level]
#		attack1
#		...
#		attackN
#	typeOne (Mon type #1)
#	typeTwo (Mon type #2)
# level (current level)
# cHP (Current HP)
# EVA (Evasion)
# ACC (Accuracy)
# attackOne (First attack set for use in battle)
# attackTwo (Second attack set for use in battle)
# attackThree (Third attack set for use in battle)
# attackFour (Fourth attack set for use in battle)
class ActiveMon():
	def __init__(self, prototype, level):
		self.original = prototype
		self.level = level
		self.cHP = self.original.attr.HP * self.level * 2
		self.EVA = 0
		self.ACC = 100

	def setAttacks(self, atkNum, attack):
		if atkNum == 1:
			self.attackOne = attack
		elif atkNum == 2:
			self.attackTwo = attack
		elif atkNum == 3:
			self.attackThree = attack
		elif atkNum == 4:
			self.attackFour = attack

