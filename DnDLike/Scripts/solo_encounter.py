import random
import math
import os
import ast
import sys
sys.path.append("Resources/")
from Scripts import create_character
from Scripts import universal_functions
from Scripts import universal_data
abilities = universal_data.abilities
from Spells import *

health = []
player = {}
monster = {}
charList = [player, monster]

def TempFunc():
	pass

def ImportNewSpell(spellName):
	exec("from Spells import " + spellName)

def AssignPlayer():
	global player
	chars = [x for x in os.listdir("Resources/Characters") if x.endswith(".txt")]
	if len(chars) == 0:
		print("You don have any characters to play as, make one and then come back")
		return(False)
	chooseCharMessage = "Your current characters are:\n"
	for i in range(len(chars)):
		chooseCharMessage += (str(i+1) + ".\t" + str(chars[i].split(".")[0]) + "\n")
	chooseCharMessage += "What character do you want to play as? "
	failString = "That is not a valid character choise, please try again: "			
	playerCharNum = universal_functions.GetValidOption(1,len(chars),failString,chooseCharMessage)
	playerFile = open("Resources/Characters/"+chars[playerCharNum-1],"r")
	for line in playerFile:
		player[line.split(":")[0]] = ast.literal_eval(line.split("\"")[1])
	playerFile.close()

def AssignMonster():
	global monster
	monsters = [x for x in os.listdir("Resources/Monsters") if x.endswith(".txt")]
	if len(monsters) == 0:
		print("You don have any monsters to play against, make one and then come back")
		return(False)
	chooseMonsMessage = "Your current monsters are:\n"
	for i in range(len(monsters)):
		chooseMonsMessage += (str(i+1) + ".\t" + str(monsters[i].split(".")[0]) + "\n")
	chooseMonsMessage += "What monster do you want to play against? "
	failString = "That is not a valid monster choise, please try again: "			
	monsterCharNum = universal_functions.GetValidOption(1,len(monsters),failString,chooseMonsMessage)
	monsterFile = open("Resources/Monsters/"+monsters[monsterCharNum-1],"r")
	for line in monsterFile:
		monster[line.split(":")[0]] = ast.literal_eval(line.split("\"")[1])
	monsterFile.close()
	

'''FireBolt,'''	
def monsterTurn():
	global abilities
	global health
	global charList
	print("monster turn:")
	damageList = abilities[random.randint(1,len(abilities))-1][1](1,0,charList)
	health[damageList[0]]+=damageList[1]
	
def playerTurn():
	global abilities
	print("player turn:")
	chooseAttackString = ("you have " + str(len(abilities)) + " different actions:\n")
	for i in range(len(abilities)):
		chooseAttackString += str(i+1) + ".\t" + abilities[i][1].__name__ + "\n"
	chooseAttackString  += "Which one do you want to use? "
	
	action = universal_functions.GetValidOption(1,len(abilities),"That is not a valid choise of an attack. Please try again: ", chooseAttackString)-1
	damageList = abilities[action][1](0,1,charList)
	health[damageList[0]]+=damageList[1]
	
def RunProgram():
	global player
	global monster
	global health
	global abilities
	global charList
	
	turnOrder = []
	input("This option is not done yet, but some of the functionality has been implemented \nPress enter to continue")
	if AssignPlayer() is not False and AssignMonster() is not False:
		health = [player['Max Hp'],monster['Max Hp']]
	
	
	
		playerInit = random.randint(1,20) + math.floor((player['Stats'][1]-10)/2)
		print("You rolled a initiativeroll of: " + str(playerInit))
		monsterInit = random.randint(1,20) + math.floor((monster['Stats'][1]-10)/2)
		print("The monster rolled a initiativeroll of :" + str(monsterInit))
		
		if playerInit > monsterInit:
			turnOrder = [playerTurn, monsterTurn]
		else:
			turnOrder = [monsterTurn, playerTurn]
	
		turnCount = 0
		while(health[0] > 0 and health[1] > 0):
			print("\n" + ("-"*30))
			print("Turn: " + str(math.floor(turnCount/2)+1) + "\tRound: " + str((turnCount%2)+1))
			print(player['Name'] + " has " + str(health[0]) + " HP left")
			print(monster['Name'] + " has " + str(health[1]) + " HP left\n")
			userTurn = turnCount%2
			turnOrder[userTurn]()
			if health[userTurn] > charList[userTurn]['Max Hp'] : health[userTurn] = charList[userTurn]['Max Hp']
			turnCount += 1
			
			
			

		if health[0] <= 0:
			print("Sorry, you lost")
		else:
			print("Congratulation, you won")
	
	input("")
	os.system('cls')