import random
import math
import os
import ast
from Scripts import create_character

classes = []

def LevelUp(Class, currLv, endLv):
	for lv in range(currLv+1,endLv+1):
		pass
		
def ASI():
	pass

def AssignDicts():
	count = 0
	global classes
	classFiles = [x for x in os.listdir("Resources/Classes") if x.lower().endswith(".txt")]
	for file in classFiles:
		fileContent = open("Resources/Classes/"+str(file),"r")
		exec("%s={}" % (str(file).split(".")[0]))
		exec("classes.append(%s)" % (str(file).split(".")[0]))
		for line in fileContent:
			string = line.split("\"")[1]
			var = ast.literal_eval(string)
			classes[count][line.split(":")[0].strip('\'')] = var
		count += 1
	
def RunProgram():
	input("This option is not done yet.\nCurrently only imports a character file into memory and prints it to the output")
	end = False
	chosenCharType = False
	while(not chosenCharType):
		chosenChar = False
		levelChoise = input("Do you want to level up a player character, monster or not level up at all 'p'/'m'/'e': ").lower()
		while(not chosenChar):
			if levelChoise == "p":
				chars = [x for x in os.listdir("Resources/Characters") if x.endswith(".txt")]
				if len(chars) == 0:
					print("There are currently no existing characters to level")
					break
				chooseCharMessage = "Your current characters are:\n"
				for i in range(len(chars)):
					chooseCharMessage += (str(i+1) + ".\t" + str(chars[i].split(".")[0]) + "\n")
				chooseCharMessage += "What character do you want to level up? "
				failString = "That is not a valid character choise, please try again: "			
				levelCharNum = create_character.GetValidOption(1,len(chars),failString,chooseCharMessage)
				levelChar = open("Resources/Characters/"+chars[levelCharNum-1],"r")

				chosenChar = True
				chosenCharType = True
			elif levelChoise == "m":
				chars = [x for x in os.listdir("Resources/Monsters") if x.endswith(".txt")]
				if len(chars) == 0:
					print("There are no currently existing characters to level")
					break
				chooseCharMessage = "Your current monsters are:\n"
				for i in range(len(chars)):
					chooseCharMessage += (str(i+1) + ".\t" + str(chars[i].split(".")[0]) + "\n")
				chooseCharMessage += "What monster do you want to level up? "
				failString = "That is not a valid monster choise, please try again: "
				levelCharNum = create_character.GetValidOption(1,len(chars),failString,chooseCharMessage)
				levelChar = open("Resources/Monsters/"+chars[levelCharNum-1],"r")
				chosenChar = True
				chosenCharType = True
			elif levelChoise == "e":
				end = True
				chosenChar = True
				chosenCharType = True
			else:
				levelChoise = input("That is not a valid choise, Please try again: ")
	
	if(not end):
		print(levelChar.read())
	
	
		input("The character has been leveled up")
	os.system('cls')