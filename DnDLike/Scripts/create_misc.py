import random
import math
import os
import sys
from Scripts import solo_encounter
from Scripts import create_character
from Scripts import universal_functions
abilities = []
abilityIDs = []
from Spells import *

def CreateWeapon():
	print("weapon")
	
def CreateSpell():
	global abilities
	global abilityIDs
	spellList = [x.split(".")[0].lower() for x in os.listdir("Resources/Spells") if x.endswith(".py")]
	spellNameChosen = False
	spellName = input("What should this new Spell be called (Choose a name that does not already exist in the spells folder)? ").replace(" ","")
	while(not spellNameChosen):
		if spellName.lower() not in spellList:
			spellNameChosen = True
		else:
			spellName = input("That spell already exsists, please choose another name ")
	for i in abilities:
		abilityIDs.append(i[0])
			
	abilityIDFound = False
	currIdTest = 1
	while(not abilityIDFound):
		if currIdTest in abilityIDs:
			currIdTest += 1
		else:
			abilityID = currIdTest
			abilityIDFound = True
			
	diceSizes = [4,6,8,10,12,20]
	damageDice = diceSizes[universal_functions.GetValidOption(1,len(diceSizes),"That is not a index in the range.\nPlease try again: ","the dice sizes are: " + str(diceSizes) + "\nChoose which index you want as damage-dice for this spell: ")-1]
		
	diceRolls = universal_functions.GetValidOption(1,1000000,"You cannot have 0, negative numbers, very high numbers or decimal numbers as nuber of dice to roll.\nPlease try again: ","Choose how many damage-dice that should be rolled for this spell: ")
	
	modifyer = universal_functions.GetValidOption(1,6,"That is not in the index.\nPlease try again: ", "[str, dex, con, int, wis, cha]\nChoose 1-6 which stat you want as modifyer for this spell ")-1
	
	
		
	file = open("Resources/Spells/" + spellName + ".py","w")
	file.write("import inspect\n")
	file.write("import math\n")
	file.write("import random\n")
	file.write("from Scripts import universal_functions\n")
	file.write("abilityID = " + str(abilityID) + "\n")
	file.write("stackList = inspect.stack()\n")
	file.write("caller = universal_functions.GetCaller(stackList)\n")
	file.write("exec('from Scripts import ' + caller)\n")
	file.write("def " + spellName + "(user, target, charList):\n")
	file.write("\tmodifyer = math.floor((charList[user]['Stats'][" + str(modifyer) + "]-10)/2)\n")
	file.write("\tattackRoll = universal_functions.rollDice(1,20,1,1,False) + modifyer\n")
	file.write("\tprint(charList[user]['Name'] + ' used " + spellName + "')\n")
	file.write("\tprint(charList[user]['Name'] + ' rolled a ' + str(attackRoll) + ' to hit')\n")
	file.write("\tif attackRoll - modifyer == 20:\n")
	file.write("\t\tdamage = 2*(universal_functions.rollDice(1," + str(damageDice) + "," + str(diceRolls) + "," + str(diceRolls) + ", False))+modifyer\n")
	file.write("\t\tprint(charList[user]['Name'] + ' rolled a critical and dealt: ' + str(damage) + ' damage')\n")
	file.write("\telif attackRoll >= charList[target]['AC']:\n")
	file.write("\t\tdamage = universal_functions.rollDice(1," + str(damageDice) + "," + str(diceRolls) + "," + str(diceRolls) + ", False)+modifyer\n")
	file.write("\t\tprint(charList[user]['Name'] + ' hit and dealt: ' + str(damage) + ' damage')\n")
	file.write("\telse:\n")
	file.write("\t\tdamage = 0\n")
	file.write("\t\tprint(charList[user]['Name'] + ' missed')\n")
	file.write("\treturn([target,-damage])\n")
	file.write("exec(caller+'.abilities.append([abilityID," + spellName + "])')\n")
	file.close()
	
	exec("from Spells import " + spellName)
	solo_encounter.ImportNewSpell(spellName)
	
	
def CreateArmor():
	print("armor")
	
def RunProgram():
	input("This option is not done yet, currently only creates a test file")
	choises = [CreateWeapon, CreateSpell, CreateArmor]
	
	choiseString = "There are " + str(len(choises)) + " different things to do in this part of the program:\n"
	for i in range(len(choises)):
		choiseString += str(i+1) + ".\t" + choises[i].__name__ + "\n"
	choiseString += "What do you want to do: "
	
	choises[universal_functions.GetValidOption(1,len(choises),"That is not a number in the list. Please try again: ",choiseString)-1]()
	input()
	os.system('cls')