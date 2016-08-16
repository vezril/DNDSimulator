#!/usr/bin/env python
from damage import DamageResistance
class Armor(object):
    def __init__(self, masterwork=False):
        self.masterwork = masterwork
        self.epic = False
        self.category = 'none'
        self.size = 'medium'
        self.enhencement = 0
        self.max_dex = None
        self.armor_bonus = 10
        self.arcane_failure = 0
        self.speed = 30
        self.totalbonus = 0
        self.enchantment = []
        self.dr = []
        self.sr = 0
        self.armor_check_penality


    def addDR(self, dr):
        self.dr.append(dr)

    def getDR(self):
        return self.dr

    def __add__(self, other):
        return self.armor_bonus + self.enhencement + other

    def __radd__(self, other):
        return self.armor_bonus + self.enhencement + other

    def __sub__(self, other):
        return self.armor_bonus + self.enhencement - other

    def __rsub__(self, other):
        return self.armor_bonus + self.enhencement - other

    def setSpeed(self, speed):
        self.speed = speed

    def enableEpic(self):
        self.epic = True

    def enableMasterwork(self):
        self.masterwork = True

    def getStatus(self):
        return self.status

    def incrementEnhencement(self):
        if ((self.totalbonus <= 9 and self.enhencement < 5) or self.epic == True):
            self.totalbonus += 1
            self.enhencement += 1
            self.status = 'success'
        else:
            self.status = 'error'

    def addEnchantment(self, name, damage=False, other=False):
        if name in self.enchantment:
            self.status = 'enchantment already present'
        elif name == 'spell resistance':
            if other == 13 and self.totalbonus <= 8:
                self.sr = 13
                self.totalbonus += 2
            elif other == 15 and self.totalbonus <= 7:
                self.sr = 15
                self.totalbonus += 3
            elif other == 17 and self.totalbonus <= 6:
                self.sr = 17
                self.totalbonus += 4
            elif other == 19 and self.totalbonus <= 5:
                self.sr = 19
                self.totalbonus += 5
            else:
                self.status = 'unknown SR level'
        elif name == 'resistance':
            if other not in ['acid','cold','fire','electricity','sonic']:
                self.status = 'Unkown resistance ' + str(other)
            self.status = 'success'
            self.enchantment.append(other + ' resistance')
            self.dr.append(DamageResistance(10, other))
        else:
            self.status = 'Unkown enchantment ' + name

class Platemail(Armor):
    def __init__(self, masterwork=False):
        super(Platemail, self).__init__(masterwork)
        self.armor_bonus = 18
        self.max_dex = 1
        self.armor_check_penality = 8
        self.arcane_failure = 0.35
        self.speed = 20

if __name__ == "__main__":
    pass
