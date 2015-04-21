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
		damage = attacker.attr.STR * attack.power
	elif attack.offAttr == Attributes.MSTR:
		damage = attacker.attr.MSTR * attack.power
	elif attack.offAttr == Attributes.DEF:
		damage = attacker.attr.DEF * attack.power
	elif attack.offAttr == Attributes.MDEF:
		damage = attacker.attr.MDEF * attack.power
	elif attack.offAttr == Attributes.SPD:
		damage = attacker.attr.SPD * attack.power
	elif attack.offAttr == Attributes.ACC:
		damage = attacker.ACC * attack.power
	elif attack.offAttr == Attributes.EVA:
		damage = attacker.EVA * attack.power
	elif attack.offAttr == Attributes.HP:
		damage = attacker.attr.HP * attack.power
	else:
		damage = attack.power

	if attacker.montype == attack.attacktype:
		damage = damage * 1.5

	if attack.defAttr == Attributes.STR:
		damage = damage / defender.attr.STR
	elif attack.defAttr == Attributes.MSTR:
		damage = damage / defender.attr.MSTR
	elif attack.defAttr == Attributes.DEF:
		damage = damage / defender.attr.DEF
	elif attack.defAttr == Attributes.MDEF:
		damage = damage / defender.attr.MDEF
	elif attack.defAttr == Attributes.SPD:
		damage = damage / defender.attr.SPD
	elif attack.defAttr == Attributes.ACC:
		damage = damage / defender.ACC
	elif attack.defAttr == Attributes.EVA:
		damage = damage / defender.EVA
	elif attack.defAttr == Attributes.HP:
		damage = damage / defender.attr.HP

	return damage

# power (The attack power. This is a multiplier on most attacks. ex 1.5)
# attackType (The type of the attack. Used for weaknesses and resistances)
# offAttr (The attribute that is used for dealing damage. Usually STR or MSTR)
# defAttr (The attribute used by the defender for blocking damage. Usually DEF or MDEF)
# priority (The higher the priority, the faster the attack. Default is 1)
# effect (A standard effect that the attack can inflict)
# effpercent (The chance fo the effect to be inflicted.)
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

