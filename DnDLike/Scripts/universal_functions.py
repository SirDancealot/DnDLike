import os
import random
import math

callers = []			
callers.append([x.split(".")[0] for x in os.listdir("Scripts") if x.endswith(".py")])
callers = callers[0]

def GetValidOption(lowRoll, highRoll, failString, message):		#a function i call everytime i have to prompt the user for a numeric input based on a list
	choise = input(message)
	chosen = False
	while(chosen == False):
		try:
			choise = int(choise)
			while(choise<lowRoll or choise>highRoll):
				choise = input(failString)
				choise = int(choise)
			chosen = True
		except ValueError:
			choise = input("That is not a valid number, please try again: ")
	return(choise)

def GetCaller(stack): #a function to find out which of the main scripts called another function
	global callers
	for FrameInfo in stack:
		caller = FrameInfo.filename.split(".")[0].split("\\")[len(FrameInfo.filename.split(".")[0].split("\\"))-1]
		if caller in callers:
			return caller
			
def rollDice(low,high,rolls,keep, individual): #rolls a dice in the 'rolls' times and only keeps the 'keep' highest rolls
	if keep > rolls:
		keep = rolls
	sum = 0
	diceRolls = []
	for rollX in range(rolls):
		diceRolls.append(random.randint(low,high))
	diceRolls.sort()
	for notToKeep in range(rolls-keep):
		del diceRolls[0]
	for roll in diceRolls:
		sum += roll
	if individual:
		return diceRolls
	else:
		return sum