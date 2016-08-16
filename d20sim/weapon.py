#!/usr/bin/env python
from damage import Damage, DamageResistance

class Weapon(object):
    def __init__(self, masterwork=False):
        self.name = 'dagger'
        self.damage = Damage(1,4,dmg_type='piercing')
        self.masterwork = masterwork
        self.hardness = 5
        self.hp = 5
        self.category = 'simple'
        self.size = 'small'
        self.enhencement = 0
        self.additional_damage = []
        self.crit_range = range(19,21)
        self.crit_mult = 2
        self.enchantment = []
        self.totalbonus = 0
        self.epic = False

        self.status = ''

    def enableEpic(self):
        self.epic = True

    def enableMasterwork(self):
        self.masterwork = True

    def getStatus(self):
        return self.status

    def incrementEnhencement(self):
        if ((self.totalbonus <= 9 and self.enhencement < 5) or self.epic == True):
            self.totalbonus += 1
            self.damage.incrementModifier()
            self.status = 'success'
        else:
            self.status = 'error'


    def roll(self):
        dmg = []
        dmg.append(self.damage.roll())

        for more in self.additional_damage:
            dmg.append(more.roll())
        return dmg

    def hitBonus(self):
        if self.masterwork == True and self.enhencement == 0:
            return 1
        else:
            return self.enhencement

    def addEnchantment(self, name, damage=False, other=False):
        if name in self.enchantment:
            self.status = 'enchantment already present'
        elif name == 'keen':
            if (self.totalbonus <= 9 or self.epic == True) and (self.type == 'piercing' or self.type == 'slashing'):
                self.crit_range = range(21-len(self.crit_range)*2,21)
                self.totalbonus += 1
                self.status == 'success'
                self.enchantment.append('keen')
            else:
                self.status = 'needs to be epic'
        elif name == 'flaming':
            if (self.totalbonus <= 9 or self.epic == True):
                self.additional_damage.append(Damage(1,6,dmg_type='fire'))
                self.totalbonus += 1
                self.status = 'success'
                self.enchantment.append('flaming')
        else:
            self.status = 'Unkown enchantment ' + name

class Longsword(Weapon):
    def __init__(self, masterwork=False):
        super(Longsword, self).__init__(masterwork)
        self.damage = Damage(1,8,dmg_type='slashing')
        self.crit_range = range(19,21)

class Scimitar(Weapon):
    def __init__(self, masterwork=False):
        super(Scimitar, self).__init__(masterwork)
        self.damage = Damage(1,6,dmg_type='slashing')
        self.crit_range = range(18,21)

class Greatsword(Weapon):
    def __init__(self, masterwork=False):
        super(Greatsword, self).__init__(masterwork)
        self.damage = Damage(3,6,dmg_type='slashing')
        self.crit_range = range(19,21)

def test():
    ls = Longsword()
    ls.addEnchantment('flaming')
    print ls.roll()


if __name__ == "__main__":
    pass
