from Spell import Spell
class Wizard:

    #currently used spell by the player 
    currentSpell=""
    # constructor 
    def __init__(self, name, health,energy,shields):
        self.spells={}
        self.name = name
        self.health = health
        self.energy = energy
        self.shields = shields
    # return the power of the current spell of the character
    def getCurrentSpellPower(self):
        return self.spells[self.currentSpell]

    # return if the charcter is dead    
    def lost(self):
        return self.health<=0
    
    # return if the character have enough power to attack using current spell
    def canAttack(self):
        return (self.energy>=self.getCurrentSpellPower())

    # return if the character have enough power to attack at all or can use shields
    def canRespond(self):
        return (self.energy>=list(self.spells.values())[1] or self.shields>0)

    # add spell to the spells of the player
    def addSpell(self,spell):
        self.spells[spell.name]=spell.power
    
    # sort the spells of the player using key value
    def sortSpells(self):
        self.spells= dict(sorted(self.spells.items(), key=lambda item: item[1]))
    
    # inflict damage to the player and substract the damage from the health
    def damage(self,damage):
        if not (self.currentSpell=="shield"):
            self.health -= damage
        
            
    
    # decrement the power of the player by the energy value of the spell or use a shield
    def attack(self):
        if self.currentSpell=="shield":
            self.shields-=1
        else:
            self.energy -= self.spells[self.currentSpell]
    
    # check if the spell exists in the players spells
    def foundSpell(self,spellToFind):
        return self.spells
