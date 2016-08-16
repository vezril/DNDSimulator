#!/usr/bin/env python
from math import floor
from armor import *

def calculateAttribute(attribute):
    return int(floor((attribute-10)/2))

class BaseStats(object):
    def __init__(self, strength=10, dex=10, con=10, intel=10, wis=10, chari=10):
        self.str = strength
        self.dex = dex
        self.con = con
        self.int = intel
        self.wis = wis
        self.cha = chari
        self.armor = Armor()
        self.additional_armor = 0
        self.name = 'default'

        self.ac = 0

    def updateAll(self):
        self.updateAC()

    def updateAC(self):
        self.ac = self.armor + calculateAttribute(self.dex) + self.additional_armor

class Character(BaseStats):
    def __init__(self, strength=10, dex=10, con=10, intel=10, wis=10, chari=10,race='human',name='default'):
        super(Character,self).__init__()
        self.race = race
        self.name = name

        self.items = []
        self.weapons = []
        self.rings = []
        self.armor = None

    def equip(self, item):
        pass

    def equipArmor(self, armr):
        self.armor = armr
        self.updateAC()




class Cleric(BaseStats):
    def __init__(self, strength=10, dex=10, con=10, intel=10, wis=10, chari=10,race='human',name='default'):
        self.armor = Armor()
        self.level = 1

    def setRace(self, race):
        self.race = race
    def setName(self, name):
        self.name = name


def test():
    t = Character()

if __name__ == "__main__":
    pass
