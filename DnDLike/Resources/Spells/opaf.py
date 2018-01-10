import math
import random
from Scripts import universal_functions
from Scripts import universal_data
abilityID = 5
def opaf(user, target, charList):
	modifyer = math.floor((charList[user]['Stats'][0]-10)/2)
	attackRoll = universal_functions.rollDice(1,20,1,1,False) + modifyer
	print(charList[user]['Name'] + ' used opaf')
	print(charList[user]['Name'] + ' rolled a ' + str(attackRoll) + ' to hit')
	if attackRoll - modifyer == 20:
		damage = 2*(universal_functions.rollDice(1,20,10,10, False))+modifyer
		print(charList[user]['Name'] + ' rolled a critical and dealt: ' + str(damage) + ' damage')
	elif attackRoll >= charList[target]['AC']:
		damage = universal_functions.rollDice(1,20,10,10, False)+modifyer
		print(charList[user]['Name'] + ' hit and dealt: ' + str(damage) + ' damage')
	else:
		damage = 0
		print(charList[user]['Name'] + ' missed')
	return([target,-damage])
universal_data.abilities.append([abilityID,opaf])
