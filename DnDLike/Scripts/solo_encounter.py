import random
import math
import os
import ast
from Scripts import create_character

health = []
player = {}
monster = {}
charList = [player, monster]

def rollDice(low,high,rolls):
	sum = 0
	for i in range(rolls):
		sum += random.randint(low,high)
	return sum

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
	playerCharNum = create_character.GetValidOption(1,len(chars),failString,chooseCharMessage)
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
	monsterCharNum = create_character.GetValidOption(1,len(monsters),failString,chooseMonsMessage)
	monsterFile = open("Resources/Monsters/"+monsters[monsterCharNum-1],"r")
	for line in monsterFile:
		monster[line.split(":")[0]] = ast.literal_eval(line.split("\"")[1])
	monsterFile.close()
	
def FireBolt(user, target):
	global charList
	global health
	intMod = math.floor((charList[user]['Stats'][3]-10)/2)
	attackRoll = rollDice(1,20,1) + intMod
	print("you used fireball")
	if attackRoll-intMod == 20:
		damage = 2*(rollDice(1,10,1))+intMod
		print("you rolled a critical and dealt: " + str(damage) + " damage")
		health[target] -= damage
	elif attackRoll >= charList[target]['AC']:
		damage = rollDice(1,10,1)+intMod
		print("you hit and dealt: " + str(damage) + " damage")
		health[target] -= damage
	else:
		print("you missed")

def SwordAttack(user, target):
	global charList
	global health
	strMod = math.floor((charList[user]['Stats'][0]-10)/2)
	print("you attacked with your sword")
	attackRoll = rollDice(1,20,1) + strMod
	if attackRoll-strMod == 20:
		damage = 2*(rollDice(1,4,1))+strMod
		print("you rolled a critical and dealt: " + str(damage) + " damage")
		health[target] -= damage
	elif attackRoll >= charList[target]['AC']:
		damage = rollDice(1,4,1)+strMod
		print("you hit and dealt: " + str(damage) + " damage")
		health[target] -= damage
	else:
		print("You missed")
	
def DaggerAttack(user, target):
	global charList
	global health
	dexMod = math.floor((charList[user]['Stats'][1]-10)/2)
	print("you attacked with your dagger")
	attackRoll = rollDice(1,20,1) + dexMod
	if attackRoll-dexMod == 20:
		damage = 2*(rollDice(1,4,1))+dexMod
		print("you rolled a critical and dealt: " + str(damage) + " damage")
		health[target] -= damage
	elif attackRoll >= charList[target]['AC']:
		damage = rollDice(1,4,1)+dexMod
		print("you hit and dealt: " + str(damage) + " damage")
		health[target] -= damage
	else:
		print("you mised")
	
def HealthPot(user, target):
	global health
	healing = rollDice(1,4,2)+2
	health[user] += healing
	print("You used a health pot and healed " + str(healing) + " health")
	if health[user] > charList[user]['Max Hp']:
		health[user] = charList[user]['Max Hp']
	
attacks = [FireBolt,SwordAttack,DaggerAttack,HealthPot]
	
def monsterTurn():
	global attacks
	print("monster turn:")
	attacks[random.randint(1,len(attacks))-1](1,0)
	
def playerTurn():
	global attacks
	print("player turn:")
	chooseAttackString = ("you have " + str(len(attacks)) + " different actions:\n")
	for i in range(len(attacks)):
		chooseAttackString += str(i+1) + ".\t" + attacks[i].__name__ + "\n"
	chooseAttackString  += "Which one do you want to do? "
	
	action = create_character.GetValidOption(1,len(attacks),"That is not a valid choise of an attack. Please try again: ", chooseAttackString)-1
	attacks[action](0,1)
	
def RunProgram():
	global player
	global monster
	global health
	
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
			print("\n---------------------------")
			print("Turn: " + str(math.floor(turnCount/2)+1) + "\tRound: " + str((turnCount%2)+1))
			print(player['Name'] + " has " + str(health[0]) + " HP left")
			print(monster['Name'] + " has " + str(health[1]) + " HP left\n")
			turnOrder[turnCount%2]()
			turnCount += 1
			
			
			

		if health[0] <= 0:
			print("Sorry, you lost")
		else:
			print("Congratulation, you won")
	
	
	input("")
	os.system('cls')