import inspect
import math
import random
from Scripts import universal_functions
abilityID = 1
stackList = inspect.stack()
caller = universal_functions.GetCaller(stackList)
exec("from Scripts import " + caller)

def FireBolt(user, target, charList):
	intMod = math.floor((charList[user]['Stats'][3]-10)/2)
	attackRoll = universal_functions.rollDice(1,20,1,1,False) + intMod
	print("You used firebolt")
	print("You rolled " + str(attackRoll)+ " to hit")
	if attackRoll-intMod == 20:
		damage = 2*(universal_functions.rollDice(1,10,1,1,False))+intMod
		print("You rolled a critical and dealt: " + str(damage) + " damage")
	elif attackRoll >= charList[target]['AC']:
		damage = universal_functions.rollDice(1,10,1,1,False)+intMod
		print("You hit and dealt: " + str(damage) + " damage")
	else:
		damage = 0
		print("You missed")
	return([target,-damage])

exec(caller+".abilities.append([abilityID,FireBolt])")