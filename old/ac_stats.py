#!/usr/bin/env python
from random import randint

class Character:
    def __init__(self):
        self.hit = []
        self.damage = None
        self.misschance = 0
        self.name = 'default'
        self.Class = 'fighter'
        self.dr = 0
        self.weaponhp = 30

    def attackPattern(self, pattern):
        self.pattern = 'attack'

    def setDR(self, dr):
        self.dr = dr

    def setMissChance(self, misschance):
        self.misschance = misschance

    def setName(self, name):
        self.name = name

    def setBAB(self, bab):
        self.bab = bab

    def setAttacks(self, attacks):
        self.attacks = attacks

    def setDamage(self, damage):
        self.damage = damage

    def setHit(self, hit):
        self.hit = hit

    def setAC(self, ac):
        self.ac = ac

    def setHP(self, hp):
        self.hp = hp
        self.maxhp = hp

    def resetHP(self):
        self.hp = self.maxhp

    def setInit(self, init):
        self.init = init

    def getsAttacked(self, roll):
        for attack in roll:
            if attack[0] >= self.ac:
                miss = randint(1,100)
                if miss <= self.misschance  and self.misschance != 0:
                    pass
                else:
                    dmg = attack[1] - self.dr
                    if dmg > 0:
                        self.hp -= attack[1]

    def getsSundered(self, attack):
        attack = attack[0]
        roll = randint(1,20)
        roll += self.attacks[0]
        if attack[0] > roll:
            self.weaponhp - attack[1]
        if self.weaponhp <= 0:
            self.damage = (1,4,5)
            return 'destroyed'
        else:
            return 'functional'

    def sunder(self):
        crit = False
        dmg = 0
        out = []
        roll = randint(1,20)
        if roll == 1:
            pass
        elif roll == 2:
            crit = True
        for dice in xrange(self.damage[0]):
            dmg += randint(1,self.damage[1])
        dmg += self.damage[2]
        if crit == True:
            dmg *= 2
        return [(roll+self.attacks[0], dmg)]

    def roll(self):
        out = []
        for attack in self.attacks:
            roll = randint(1,20)
            dmg = 0
            if roll == 20:
               for dice in xrange(self.damage[0]*2):
                   dmg += randint(1,self.damage[1])
               dmg += self.damage[2]*2
            elif roll == 1:
                dmg = 0
                out.append((attack,dmg))
                break
            else:
                for dice in xrange(self.damage[0]):
                    dmg += randint(1,self.damage[1])
                dmg += self.damage[2]
            out.append((roll+attack,dmg))
        return out

def runBattle(battles, character1, character2):
    Wins = {}
    Wins[character1.name] = 0
    Wins[character2.name] = 0
    character1.resetHP()
    character2.resetHP()
    for battle in xrange(battles):
        #print "Battle " + str(battle+1)
        round = 0
        while True:
            # For this sim, assume goes second
            character1.getsAttacked(character2.roll())
            if character1.hp <= 0:
                Wins[character2.name]+=1
                break
            character2.getsAttacked(character1.roll())
            if character2.hp <=0:
                Wins[character1.name]+=1
                break
        character2.resetHP()
        character1.resetHP()
    return Wins

if __name__ == "__main__":
    battles = 10000
    Jin = Character()
    Jin.setAttacks([25,20,15])
    Jin.setDamage((1,8,14))
    Jin.setAC(33)
    Jin.setHP(133)
    Jin.setInit(-1)
    Jin.setName('Jin')
    Jin.setDR(6)

    BadGuy = Character()
    BadGuy.setAttacks([25,20,15])
    BadGuy.setDamage([3,6,15])
    BadGuy.setAC(29)
    BadGuy.setHP(140)
    BadGuy.setInit(2)
    BadGuy.setName('HalfDragon')

    battles = 10000

    Wins = runBattle(battles,Jin,BadGuy)
    print 'Jin AC 33, BadGuy AC 29'
    print 'Jin Wins ' + str(float(Wins['Jin']) / float(Wins['HalfDragon']+Wins['Jin']))

    Jin.setDR(0)
    Wins = runBattle(battles,Jin,BadGuy)
    print 'Jin AC 33, no DR, BadGuy AC 29'
    print 'Jin Wins ' + str(float(Wins['Jin']) / float(Wins['HalfDragon']+Wins['Jin']))

    Jin.setDR(6)
    Jin.setAC(30)
    Wins = runBattle(battles,Jin,BadGuy)
    print 'Jin AC 30, BadGuy AC 29'
    print 'Jin Wins ' + str(float(Wins['Jin']) / float(Wins['HalfDragon']+Wins['Jin']))

    Jin.setMissChance(20)
    Wins = runBattle(battles,Jin,BadGuy)
    print 'Jin AC 30, miss chance 20%, BadGuy AC 29'
    print 'Jin Wins ' + str(float(Wins['Jin']) / float(Wins['HalfDragon']+Wins['Jin']))

    Jin.setMissChance(50)
    Wins = runBattle(battles,Jin,BadGuy)
    print 'Jin AC 30, miss chance 50%, BadGuy AC 29'
    print 'Jin Wins ' + str(float(Wins['Jin']) / float(Wins['HalfDragon']+Wins['Jin']))

    Jin.setMissChance(20)
    Jin.setAC(33)
    Wins = runBattle(battles,Jin,BadGuy)
    print 'Jin AC 33, miss chance 20%, BadGuy AC 29'
    print 'Jin Wins ' + str(float(Wins['Jin']) / float(Wins['HalfDragon']+Wins['Jin']))

    Jin.setAttacks([25,25,20,15])
    Jin.setMissChance(0)
    Jin.setAC(30)
    Wins = runBattle(battles,Jin,BadGuy)
    print 'Jin AC 30, Additonal attack, BadGuy AC 29'
    print 'Jin Wins ' + str(float(Wins['Jin']) / float(Wins['HalfDragon']+Wins['Jin']))

    Jin.setAttacks([25,20,15])
    Jin.setHP(133+26)
    Jin.setMissChance(0)
    Jin.setAC(33)
    Wins = runBattle(battles,Jin,BadGuy)
    print 'Jin AC 33, more HP, BadGuy AC 29'
    print 'Jin Wins ' + str(float(Wins['Jin']) / float(Wins['HalfDragon']+Wins['Jin']))

    Jin.setAC(30)
    Wins = runBattle(battles,Jin,BadGuy)
    print 'Jin AC 30, more HP, BadGuy AC 29'
    print 'Jin Wins ' + str(float(Wins['Jin']) / float(Wins['HalfDragon']+Wins['Jin']))

    Jin.setHP(133)
    Jin.setAC(33)
    Jin.setDamage((2,6,18))
    Wins = runBattle(battles,Jin,BadGuy)
    print 'Jin AC 33, w/ THW, BadGuy AC 29'
    print 'Jin Wins ' + str(float(Wins['Jin']) / float(Wins['HalfDragon']+Wins['Jin']))

    Jin.setHP(133)
    Jin.setAC(29)
    Jin.setDamage((2,6,18))
    Wins = runBattle(battles,Jin,BadGuy)
    print 'Jin AC 33, w/ THW without shield, BadGuy AC 29'
    print 'Jin Wins ' + str(float(Wins['Jin']) / float(Wins['HalfDragon']+Wins['Jin']))

'''
0: 6
1: 7+1
    Bless
    Shield of Faith (Persisted)
    Domain: Expedious Retreat
2: 6+1
    Silence
    Delay Poison
    Gentle Repose
    Wave of Grief
    Remove Paralysis
    Undetectable Alignement
    Domain: Cat's grace
3: 5+1
    Magic Vestment
    Magic Vestment
    Downdraft
    Prayer
    Blindness/Deafened
    Domain: Blur
4: 4+1
    Divine Power (Persisted)
    Great, Magic Weapon
    Death Ward
    Restoration
    Domain: Haste
5: 3+1
    Rigtheous Might (Persisted)
    Break Enchantment
    True Seeing
    Domain: Spell Resistance
6: 1+1
    Bear's Endurance, Mass
    Domain: Antimagic Field
'''
