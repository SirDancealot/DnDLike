import inspect
import math
import random
from Scripts import universal_functions
abilityID = 2
stackList = inspect.stack()
caller = universal_functions.GetCaller(stackList)
exec("from Scripts import " + caller)

def SmallHealthPot(user, target, charList):
	healing = universal_functions.rollDice(1,4,2)+2
	print("You used a health pot and healed " + str(healing) + " health")
	return([user,healing])

exec(caller+".abilities.append([abilityID,SmallHealthPot])")