#!/usr/bin/env python
from random import randint

class Damage(object):
    def __init__(self, dice, dice_type, modifier=0, dmg_type='normal'):
        self.dice = dice
        self.dice_type = dice_type
        self.modifier = modifier
        self.dmg_type = dmg_type
        self.dmg = 0

    def incrementModifier(self):
        self.modifier += 1

    def updateModifier(self, modifier):
        self.modifier = modifier

    def roll(self):
        dmg = 0
        for i in xrange(self.dice):
            dmg += randint(1,self.dice_type)
        dmg += self.modifier
        if dmg<0:
            dmg = 0
        return (dmg,self.dmg_type)

class DamageResistance(object):
    def __init__(self,value,res_type):
        self.res_type = res_type
        self.value = value

    '''
    Attacks come in the form of [(dmg,type),...]
    '''
    def applyDR(self,attacks):
        new_attacks = []
        for attack in attacks:
            if attack[1] == self.res_type:
                new_attacks.append(attack)
            else:
                dmg = attack[0] - self.value
                if dmg < 0:
                    dmg = 0
                new_attacks.append((dmg,attack[1]))
        return new_attacks

if __name__ == "__main__":
    pass
