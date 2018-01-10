#import inspect
import math
import random
from Scripts import universal_functions
from Scripts import universal_data
abilityID = 3
#stackList = inspect.stack()
#caller = universal_functions.GetCaller(stackList)
#exec("from Scripts import " + caller)

def SwordAttack(user, target, charList):
	strMod = math.floor((charList[user]['Stats'][0]-10)/2)
	attackRoll = universal_functions.rollDice(1,20,1,1,False) + strMod
	print("You attacked with your sword")
	print("You rolled " + str(attackRoll)+ " to hit")
	if attackRoll-strMod == 20:
		damage = 2*(universal_functions.rollDice(1,4,1,1,False))+strMod
		print("You rolled a critical and dealt: " + str(damage) + " damage")
	elif attackRoll >= charList[target]['AC']:
		damage = universal_functions.rollDice(1,4,1,1,False)+strMod
		print("You hit and dealt: " + str(damage) + " damage")
	else:
		damage = 0
		print("You missed")
	return([target,-damage])

universal_data.abilities.append([abilityID,SwordAttack])