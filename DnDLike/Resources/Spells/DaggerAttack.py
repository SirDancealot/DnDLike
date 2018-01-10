#import inspect
import math
import random
from Scripts import universal_data
from Scripts import universal_functions
abilityID = 4
#stackList = inspect.stack()
#caller = universal_functions.GetCaller(stackList)
#exec("from Scripts import " + caller)

def DaggerAttack(user, target, charList):
	dexMod = math.floor((charList[user]['Stats'][1]-10)/2)
	attackRoll = universal_functions.rollDice(1,20,1,1,False) + dexMod
	print("You attacked with your dagger")
	print("You rolled " + str(attackRoll)+ " to hit")
	if attackRoll-dexMod == 20:
		damage = 2*(universal_functions.rollDice(1,4,1,1,False))+dexMod
		print("You rolled a critical and dealt: " + str(damage) + " damage")
	elif attackRoll >= charList[target]['AC']:
		damage = universal_functions.rollDice(1,4,1,1,False)+dexMod
		print("You hit and dealt: " + str(damage) + " damage")
	else:
		damage = 0
		print("You missed")
	return([target,-damage])

universal_data.abilities.append([abilityID,DaggerAttack])