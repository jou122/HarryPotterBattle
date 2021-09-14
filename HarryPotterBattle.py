from Wizard import Wizard
from Spell import Spell
import os

import xml.etree.ElementTree as ET


script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

rel_xml_path= "Output.xml" # Relative xml file path
abs_xml_path = os.path.join(script_dir, rel_xml_path) # Absoulte path

rel_spells_path = "spells.txt" # Relative path
abs_spells_path = os.path.join(script_dir, rel_spells_path) # Absoulte path

'''#################
the word shield is edited in spells.txt 
and the name voldemort is edited in the output
#################'''




round=1 # round count


def printReport(): #function to print the game report
    print ('{:<10}'.format("Round "),round,'{:^10}'.format("Harry"),'{:^30}'.format("Voldemort"))
    print ('{:<10}'.format("Health :"),'{:<10}'.format(Harry.health),'{:^30}'.format(Voldemort.health))
    print ('{:<10}'.format("Energy :"),'{:<10}'.format(Harry.energy),'{:^30}'.format(Voldemort.energy))

    
    
    roundXml,set("Num",str(round))
    roundXml.text="\n\n"

    player_1 = ET.SubElement(round, Harry.name)
    player_1.text=Harry.name
    player_1.set('\nHealth', str(Harry.health))
    player_1.set('\nEnergy', str(Harry.energy))
    player_1.set('\nNo of shields', str(Harry.shields))
    

    player_2 = ET.SubElement(round, Voldemort.name)
    player_2.text=Voldemort.name
    player_2.set('\nHealth', str(Voldemort.health))
    player_2.set('\nEnergy', str(Voldemort.energy))
    player_2.set('\nNo of shields', str(Voldemort.shields))

    
    





def battle(): # function to start the battle between the players if they have enough power or have shields
    Harry.attack()

    Voldemort.attack()

    damage = abs(Harry.getCurrentSpellPower()-Voldemort.getCurrentSpellPower())

    if Harry.getCurrentSpellPower()>Voldemort.getCurrentSpellPower():
        Voldemort.damage(damage)
        if Voldemort.health<0:
            Voldemort.health=0
    else:
        Harry.damage(damage)
        if Harry.health<0:
            Voldemort.health=0

    printReport()



playersXml = ET.Element('Players\n')



# Creating first player
Harry=Wizard("Harry Potter",100,500,3)


player_1 = ET.SubElement(playersXml, '\nLight_Wizard')
player_1.text=Harry.name
player_1.set('\nHealth', str(Harry.health))
player_1.set('\nEnergy', str(Harry.energy))
player_1.set('\nNo of shields', str(Harry.shields))
player_1_spells=ET.SubElement(player_1,"Spell Book")
spellXml=ET.SubElement(player_1_spells,"Spell")

for spellName,spllValue in Harry.spells.items():
    
    spellXml.set("Name",spellName)
    spellXml.set("Power",spllValue)
    player_1_spells.append(spellXml)



# Creating second player
Voldemort=Wizard("Lord Voldemort",100,500,3)

player_2 = ET.SubElement(playersXml, '\nDark_Wizard')
player_2.text=Voldemort.name
player_2.set('\nHealth', str(Voldemort.health))
player_2.set('\nEnergy', str(Voldemort.energy))
player_2.set('\nNo of shields', str(Voldemort.shields))
player_2_spells=ET.SubElement(player_1,"Spell Book")
spellXml2=ET.SubElement(player_2_spells,"Spell")

for spellName,spllValue in Harry.spells.items():
    
    spellXml2.set("Name",spellName)
    spellXml2.set("Power",spllValue)
    player_2_spells.append(spellXml)





# opening the text file to assign spells to each wizard
with open(abs_spells_path,'r') as file:
    # reading each line    
    for line in file:
        # reading the three word separitly
        word1,word2,word3 = line.split()
        word3=int(word3)
        word2=word2.lower()
        if word1=="A" or word1=="H": # assign for harry
            Harry.addSpell(Spell(word2,word3))              
        if word1=="A" or word1=="V": # assign for voldemort
            Voldemort.addSpell(Spell(word2,word3)) 




# sort the spells to find if the char have enough power to attack
Harry.sortSpells()
Voldemort.sortSpells()


playersText = ET.tostring(playersXml, encoding='unicode', method='xml')



roundsXML=ET.Element('Rounds')
roundsXML.text="\n"

# Game
while(True):
    flag=0

    roundXml=ET.SubElement(roundsXML,'Round'+str(round))


    # if Harry lost the game end
    if Harry.lost():
        print('{:^50}'.format("Voldemort Is The Winner"))
        roundXml,set("Num",str(round))
        roundXml.text="\nVoldemort Is The Winner\n"
        break
        


    # if voldemort lost game end
    elif Voldemort.lost():
        print('{:^50}'.format("Harry IS The Winner"))
        roundXml.set("Num",str(round))
        roundXml.set("state","Last")
        roundXml.text="\nHarry Is The Winner\n"
        break
        
    



    # try taking the input handeling exception of entering invalid data
    try:
        Harry.currentSpell,Voldemort.currentSpell=input("Enter the two spells (Harry then Voldemort):\n").split()
    except ValueError:
        print("not valid input")
        roundXml.set("State","invalid")
        roundXml.text="\nnot valid input\n"
        continue
        flag=1


    #set to lower to handel case sensetivity 
    Harry.currentSpell=Harry.currentSpell.lower()
    Voldemort.currentSpell=Voldemort.currentSpell.lower()



    # check if the entered spell isn't in harry's spells
    if not(Harry.currentSpell in Harry.spells):
        print("spell not found in Harry's speels")
        roundXml.set("State","invalid")
        roundXml.text="\nspell not found in Harry's speels\n"
        continue
        flag=1



    # check if the entered spell isn't in voldemort's spells
    if not(Voldemort.currentSpell in Voldemort.spells):
        print("spell not found voldemort's spells")
        roundXml.set("State","invalid")
        roundXml.text="\nspell not found in voldemort's speels\n"
        continue
        flag=1



    # if the player cann't attack using the current spell but still can responde
    if not (Harry.canAttack()) and Harry.canRespond():
        print("Harry can't use this spell because he don't have enough power")
        roundXml.set("State","invalid")
        roundXml.text="\nHarry can't use this spell because he don't have enough power\n"
        continue
        flag=1
    
    if not (Voldemort.canAttack()) and Voldemort.canRespond():
        print("Voldemort can't use this spell because he don't have enough power")
        roundXml.set("State","invalid")
        roundXml.text="\nVoldemort can't use this spell because he don't have enough power\n"
        continue
        flag=1


     # if both players cann't respond
    if not (Voldemort.canRespond()) and not (Harry.canRespond()):
        print("Stalemate")
        roundXml.set("State","Stalemate")
        roundXml.text="\nStalemate\n"
        break



     # if only one player cann't respond
    elif not Harry.canRespond():
        print("Harry can't responde")
        roundXml.set("State","Stalemate")
        roundXml.text="\nHarry can't responde\n"
        break
    
    elif not Voldemort.canRespond():
        print("voldemort can't responde")
        roundXml.set("State","Stalemate")
        roundXml.text="\nvoldemort can't responde\n"
        break
    



    # if tried to apply shield  when the player has already consumed  his shields
    if Harry.currentSpell=="shield" and Harry.shields<=0:
        print("Harry can't use shields")
        roundXml.set("State","invalid")
        roundXml.text="\nHarry can't use shields\n"
        continue
        flag=1

    if Voldemort.currentSpell=="shield" and Voldemort.shields<=0:
        print("Voldemort can't use shields")
        roundXml.set("State","invalid")
        roundXml.text="\nVoldemort can't use shields\n"
        continue
        flag=1



    if not flag: #if none of the above cases happened battle begins
      battle()
      round += 1
      
      roundsXML.append(roundXml)

roundsXML.append(roundXml)
roundsText=ET.tostring(roundsXML, encoding='unicode', method='xml')

with open(abs_xml_path, "w") as f:
    f.write(playersText+"\n\n\n"+roundsText)