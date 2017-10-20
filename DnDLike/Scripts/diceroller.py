import math
import random
import os
from Scripts import universal_functions

def RunProgram():
	print("When rolling the format is: '[rolls]d[sides]<k[numDiceToKeep]><+/-[modifyers]>'")
	rolling = True
	while(rolling):
		numDice = ""
		roll = ""
		adition = ""
		dice = ""
		keep = ""
		
		
		roll = input("What dice-roll do you want to make: ").lower()
		try:
			numDice,roll = roll.split("d")
			if "+" in roll:
				roll,adition = roll.split("+")
			elif "-" in roll:
				roll,adition = roll.split("-")
			else:
				adition = "0"
			if "k" in roll:
				dice,keep = roll.split("k")
			else:
				keep = numDice
				dice = roll
				
				
			numDice = int(numDice)
			adition = int(adition)
			dice = int(dice)
			keep = int(keep)
			
			total = universal_functions.rollDice(1,dice,numDice,keep)
			
			print("You rolled a total of: " + str(total+adition))
			
		except ValueError:
			print("Your input was not a valid string")
	
	
	
		keepRolling = input("Do you want to keep rolling (y/n)? ").lower()
		if keepRolling not in ["y","yes","true","","t"]:
			rolling = False