#!/usr/bin/python
from Standards import AutoNumber, Effects, Types, Attributes

class Attacks(AutoNumber):
	#normal
	Struggle = ()
	QuickAttack = ()	
	#fire
	FireBreath = ()
	Explosion = ()
	#water
	WaterBall = ()
	#wind
	Tornado = ()
	#earth
	Earthquake = ()
	Mudball = ()

def getAttack(attackNum):
	if attackNum == Attacks.QuickAttack:
		return BasicAttack(1.5, Types.Normal, Attributes.STR, Attributes.DEF, 2, Effects.NoEffect, 0)
	else:  #Struggle
		return BasicAttack(1.0, Types.Normal, Attributes.STR, Attributes.DEF, 1, Effects.Recoil, 20)

def CalculateDamage(attack, attacker, defender):
	damage = 0
	if attack.offAttr == Attributes.STR:
		damage = attacker.str * attack.power
	elif attack.offAttr == Attributes.MSTR:
		damage = attacker.mstr * attack.power
	elif attack.offAttr == Attributes.DEF:
		damage = attacker.DEF * attack.power
	elif attack.offAttr == Attributes.MDEF:
		damage = attacker.mdef * attack.power
	elif attack.offAttr == Attributes.SPD:
		damage = attacker.spd * attack.power
	elif attack.offAttr == Attributes.ACC:
		damage = attacker.acc * attack.power
	elif attack.offAttr == Attributes.EVA:
		damage = attacker.eva * attack.power
	elif attack.offAttr == Attributes.HP:
		damage = attacker.hp * attack.power
	else:
		damage = attack.power

	if attacker.montype == attack.attacktype:
		damage = damage * 1.5

	if attack.defAttr == Attributes.STR:
		damage = damage / defender.str
	elif attack.defAttr == Attributes.MSTR:
		damage = damage / defender.mstr
	elif attack.defAttr == Attributes.DEF:
		damage = damage / defender.DEF
	elif attack.defAttr == Attributes.MDEF:
		damage = damage / defender.mdef
	elif attack.defAttr == Attributes.SPD:
		damage = damage / defender.spd
	elif attack.defAttr == Attributes.ACC:
		damage = damage / defender.acc
	elif attack.defAttr == Attributes.EVA:
		damage = damage / defender.eva
	elif attack.defAttr == Attributes.HP:
		damage = damage / defender.hp

	return damage

class BasicAttack():
	def __init__(self, power, attackType, offAttr, defAttr, priority, effect, effpercent):
		self.power = power
		self.attackType = attackType
		self.offAttr = offAttr
		self.defAttr = defAttr
		self.priority = priority
		self.effect = effect
		self.effpercent = effpercent
		
	def extraEffect(self, attacker):
		return 0

