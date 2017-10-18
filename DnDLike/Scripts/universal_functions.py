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

def GetCaller(stack):
	global callers
	for FrameInfo in stack:
		caller = FrameInfo.filename.split(".")[0].split("\\")[len(FrameInfo.filename.split(".")[0].split("\\"))-1]
		if caller in callers:
			return caller
			
def rollDice(low,high,rolls):
	sum = 0
	for i in range(rolls):
		sum += random.randint(low,high)
	return sum