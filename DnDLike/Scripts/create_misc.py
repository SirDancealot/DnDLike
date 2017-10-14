import random
import math
import os
from Scripts import create_character

def CreateWeapon():
	print("weapon")
	
def CreateSpell():
	print("spell")
	file = open("Resources/Spells/test.py","w")
	file.write("abilityID=5\nabilityName='Fire Bolt'\ndamagelist=[[8,2,acid],[damage,fire]]")
	
	
def CreateArmor():
	print("armor")


def RunProgram():
	input("This option is not done yet")
	choises = [CreateWeapon, CreateSpell, CreateArmor]
	
	choiseString = "There are " + str(len(choises)) + " different things to do in this part of the program:\n"
	for i in range(len(choises)):
		choiseString += str(i+1) + ".\t" + choises[i].__name__ + "\n"
	choiseString += "What do you want to do: "
	
	choises[create_character.GetValidOption(1,len(choises),"That is not a number in the list. Please try again: ",choiseString)-1]()
	input()
	os.system('cls')