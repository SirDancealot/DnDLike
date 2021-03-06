#Importing modules
import random
import math
import os
from Scripts import universal_functions
from Scripts import level_up

#defining global varables
name = ""
AC = 0
health = 0
stats = []		#Stat format is: [Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma]
movementSpeed = 0
level = 0
charType = ""
race = ""
subRace = ""
resistances = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #resistance format is: [acid, phys bludgeoning, magic bludgeoning, cold, fire, force, lightning, necrotic, phys piercing, magic piercing, poison, psychic, radiant, phys slashing, magic slashing, thunder]	
size = ""
sizeFlavor = ""
langs = []
age = 0
alignment = ""
abilities = []
traits  = []
proficiencies = []
spells = []
equipment = []
charClass = ""
profBonus = 0


races = []
subRaces = []
classes = level_up.classes
classDict = {}


#Defining functions
def saveCharacter(name, stats, movementSpeed, level, charType, race, resistances, size, sizeFlavor, langs, age, alignment, subRace, abilities, proficiencies, traits, charClass, health, AC, equipment, profBonus):		#Saves the character you have created in a txt document in one of the folders depending on if your char is a pleyer char or an enemie
	if charType == "m":
		file = open("Resources/Monsters/"+str(name)+".txt","w")
	else:
		file = open("Resources/Characters/"+str(name)+".txt","w")
		
	file.write("Name:\t" + "\"'" + name + "'\"" + "\n")
	file.write("Class:\t\"'" + charClass + "'\"\n")
	file.write("Age:\t\"" + str(age) + "\"\n")
	file.write("Race:\t\"'" + race + subRace + "'\"\n")
	file.write("Max Hp:\t\"" + str(health) + "\"\n")
	file.write("AC:\t\"" + str(AC) + "\"\n")
	file.write("Proficieny bonus:\t\"" + str(profBonus) + "\"\n")
	file.write("Alignment:\t\"'" + alignment + "'\"\n")
	file.write("Languages:\t\"" + str(langs) + "\"\n")
	file.write("Speed:\t\"" + str(movementSpeed) + "\"\n")
	file.write("Size:\t\"'"+size+"'\"\tFlavor size:\t"+str(sizeFlavor)+" Feet\n")
	file.write("Level:\t" + "\"" + str(level) + "\"" + "\n")
	file.write("Stats:\t\"" + str(stats) + "\"\tFormat: [str, dex, con, int, wis, cha]\n")
	file.write("Resistances:\t\""+str(resistances)+"\"\tformat: [acid, phys bludgeoning, magic bludgeoning, cold, fire, force, lightning, necrotic, phys piercing, magic piercing, poison, psychic, radiant, phys slashing, magic slashing, thunder]\n")
	file.write("Abilitie ids:\t\"" + str(abilities) + "\"\n")
	file.write("Proficiencies:\t\"" + str(proficiencies)+ "\"\n")
	file.write("Traits:\t\""+ str(traits) +"\"\n")
	file.write("Equipment:\t\"" + str(equipment) + "\"\n")
	
	
	if charType == "m":
		input("Your character has been saved under: " + "Resources/Monsters/"+name+".txt")
	else:
		input("Your character has been saved under: " + "Resources/Characters/"+name+".txt")

def statBuyToPoint(stat):		#only being called in PointBuyStats() to convert stat to point cost
	points = [0,1,2,3,4,5,7,9]
	return(points[stat-8])
		
def RollStats():		#one of the three ways the stats can be filled out, this one uses the ranom method
	global stats
	statValues = []
	print("You have chossen to roll your stats.\nThe format for rolling stats is 4d6k3")
	for numberOfStats in range(6):
		tempStat = []
		statSum = 0
		for rollsPerStat in range(4):
			tempStat.append(random.randint(1,6))
		tempStat.sort()
		tempStat[0]=0
		for num in tempStat:
			statSum+=num
		statValues.append(statSum)
		statValues.sort()
	print("Your stat rolls are: " + str(statValues))
	count = 0
	for stat in ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]:
		choise = universal_functions.GetValidOption(1,6-count,"That is not a valid choise, please try again: ","Choose which index of the stat rolls you want as " + stat + ". Choose in range 1-" + str(6-count) + ": ")
		choise -= 1
		stats.append(statValues[choise])
		print("You have choosen " + str(statValues[choise]) + " for " + str(stat))
		del statValues[choise]
		if(len(statValues)!=0):
			print("Your remaining rolls are: " + str(statValues))
		count += 1

def PointBuyStats():	#one of the three ways the stats can be filled out, this one uses a system where the stat cost a price depending on how big you want the stat to be
	global stats
	pointsLeft = 27
	print("You have chosen to buy your points\nYou have a total of 27 points, the price of the different ability scores are as follows\nScore:\t\t8\t9\t10\t11\t12\t13\t14\t15\nPrice:\t\t0\t1\t2\t3\t4\t5\t7\t9")
	count = 0
	for stat in ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]:
		chosen = False
		choise = input("Choose what stat roll you want for " + stat + " that you also have enough points left for: ")
		while(chosen == False):
			try:
				choise = int(choise)
				while(choise<8 or choise>15 or statBuyToPoint(choise)> pointsLeft):
					choise = input("Either that is not a value you can choose, or it costs too much for you to buy that stat.\nPlease try again: ")
					choise = int(choise)
				chosen = True
			except ValueError:
				choise = input("That is not a number. Please try again: ")
		stats.append(choise)
		print("You have choosen " + str(choise) + " for " + stat)
		pointsLeft -= int(statBuyToPoint(int(choise)))
		if(len(stats)!=6):
			print("Your have: " + str(pointsLeft) + " points left")
		count += 1
	
def PredefinedStats():	#one of the three ways the stats can be filled out, this one you pick each stat from a list of values
	global stats
	statValues = [15, 14, 13, 12, 10, 8]
	print("You have chosen to pick stats form the predefined stat list")
	print("The predefined stat list is: " + str(statValues))
	
	count = 0
	for stat in ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]:
		choise = universal_functions.GetValidOption(1,(6-count), "You did not choose a value in that range.\nChoose a value in the range 1-"+str(6-count)+": ",("Choose which index of the stat rolls you want as " + stat + ". Choose in range 1-" + str(6-count) + ": "))-1
		stats.append(statValues[choise])
		print("You have choosen " + str(statValues[choise]) + " for " + stat)
		del statValues[choise]
		if(len(statValues)!=0):
			print("Your remaining rolls are: " + str(statValues))
		count += 1

def AssignRace():	#Assigning specific race values and traits
	global race
	global races
	global subRaces
	global stats
	global movementSpeed
	global resistances
	global size
	global sizeFlavor
	global langs
	global age
	
	raceDict = races[universal_functions.GetValidOption(1,9,"That is not a valid race-number from the list\nPlease try again: ", "What race do you want to play?\n1.\tDragonborn\n2.\tDwarf\n3.\tElf\n4.\tGnome\n5.\tHalf-Elf\n6.\tHalf-Orc\n7.\tHalfling\n8.\tHuman\n9.\tTiefling\nChoose 1/2/3/4/5/6/7/8/9: ")-1]
	race = raceDict['Name']
	if 'subRaceIndex' in raceDict:
		for subRaceDict in subRaces:
			if subRaceDict['Index'] == raceDict['subRaceIndex']:
				AssignSubRace(subRaceDict)
		#AssignSubRace(subRaces[raceDict['subRace']])
	
	for i in raceDict['statBoost']:
		if type(i[0]) != int:
			stats[i[0](1,6,"That is not a valid ability score. Please try again: ","Choose which ability score you want to improve by 1\n1.\tStrength\n2.\tDexteriay\n3.\tConstitution\n4.\tIntelligence\n5.\tWisdom\n6.\tCharisma\nChoose an option: ")-1]+=i[1]
		else:
			stats[i[0]] += i[1]
	movementSpeed = raceDict['speed']
	size = raceDict['size']
	sizeFlavor = universal_functions.GetValidOption((raceDict['sizeFlavor'][0])-1, (raceDict['sizeFlavor'][1])+1, "That is not a valid size in feet. Please try again: ", "A typical " + race.lower() + " is between " + str(raceDict['sizeFlavor'][0]) + " and " + str(raceDict['sizeFlavor'][1]) + " feet tall. \nI have given you a foot leway on each side to choose from. \nHow tall do you want your character to be? ")
	for lang in raceDict['langs']:
		langs.append(lang)
	age = universal_functions.GetValidOption(math.floor((raceDict['age'][0]*2)/3), math.floor((raceDict['age'][1]*2)/3), "That is either too young or too old for a " + race.lower() + "to be usefull for a party.\nPlease choos an age between " + str(math.floor((raceDict['age'][0]*2)/3)) + " and " + str(math.floor((raceDict['age'][1]*2)/3)) + " years: ", "Most " + race.lower() + "s becomes mature at age " + str(raceDict['age'][0]) + " and die around the age of " + str(raceDict['age'][1]) + ". \nYou can choose an age for this character in the range: " + str(math.floor((raceDict['age'][0]*2)/3)) + " to " + str(math.floor((raceDict['age'][1]*2)/3)) + " years: ")
	if 'resist' in raceDict:
		resistances[raceDict['resist']] = 1
	if 'traits' in raceDict:
		AddTrait(raceDict['traits'])
	
def AssignSubRace(subRaceDict):
	global subRace
	global race
	global races
	global stats
	global movementSpeed
	global resistances
	global size
	global sizeFlavor
	global langs
	global age
	
	subRaces = []
	for key in subRaceDict:
		subRaces.append(key)
	numSubRaces = len(subRaces)
	choiseString = ("The race: " + race + " has " + str(numSubRaces-1) + " sub-races which are as follows:\n")
	for i in range(1,numSubRaces):
		choiseString += (str(i)+".\t"+subRaces[i]+"\n")
	choiseString += "Which sub-race do you want this character to be? "
	subRace = subRaces[universal_functions.GetValidOption(1,numSubRaces-1,"That is not a subrace-number on the list",choiseString)]
	
	subRaceBonuses = ["resistances", "abilities", "stats", "proficiencies", "movement", "traits", "spell"]
	subRaceBonusFunctions = [AddRes, AddAbility, ASI, AddProficiencie, SetSpeed, AddTrait, AddSpell]
	
	for subRaceAbility in subRaceDict[subRace]:
		try:
			subRaceBonusFunctions[subRaceBonuses.index(subRaceAbility[0])](subRaceAbility[1])
		except ValueError:
			pass
			
	
	subRace = ", " + subRace

def AddRes(resToAdd):
	global resistances
	resistances[resToAdd] = 1
	
def AddAbility(abilityId):
	global abilities
	for ability in abilityId:
		abilities.append(ability)
	
def ASI(scoreImprovement):
	global stats
	stats[scoreImprovement[0]] += scoreImprovement[1]
	
def AddProficiencie(profs):
	global proficiencies
	for prof in profs:
		proficiencies.append(prof)
	
def SetSpeed(speed):
	global movementSpeed
	movementSpeed = speed
	
def AddTrait(addTraits):
	global traits
	for trait in addTraits:
		traits.append(trait)
		
def AddSpell(addSpells):
	global spells
	for spell in addSpells:
		spells.append(spell)
	
def AssignDicts():	#a function to assign all my dictionaries for races, calsses and so on to a list of each type
	global races
	global subRaces
				
	races = [eval(open("Resources/Races/"+x,'r').read()) for x in os.listdir("Resources/Races/") if x.endswith(".txt")]
	subRaces = [eval(open("Resources/Races/SubRaces/"+x,'r').read()) for x in os.listdir("Resources/Races/SubRaces/") if x.endswith(".txt")]
	
def AssignAlignment():
	global alignment
	alignments = ["Lawful good","Neutral good","Chaotic good","Lawful neutral","True neutral","Chaotic neutral","Lawful evil","Neutral evil","Chaotic evil"]
	alignment = alignments[universal_functions.GetValidOption(1, 9, "That value is not in the list alignment list. Please try again: ", "Choose which alignment you're character will have\n" + "1.\t" + str(alignments[0] ) + "\n" + "2.\t" + str(alignments[1] ) + "\n" + "3.\t" + str(alignments[2] ) + "\n" + "4.\t" + str(alignments[3] ) + "\n" + "5.\t" + str(alignments[4] ) + "\n" + "6.\t" + str(alignments[5] ) + "\n" + "7.\t" + str(alignments[6] ) + "\n" + "8.\t" + str(alignments[7] ) + "\n" + "9.\t" + str(alignments[8] ) + "\n" + "What alignment do you want? ")-1]

def AssignClass():
	global charClass
	global classes
	global classDict
	
	
	classMessage = ("There are " + str(len(classes)) + " classes which are:\n")
	for i in range(1,len(classes)+1):
		classMessage += (str(i) + ".\t" + classes[i-1]['Name'] + "\n")
	classMessage += "Which class do you want to play? "
	classDict = classes[universal_functions.GetValidOption(1,len(classes),"That is not a class in the range",classMessage)-1]
	charClass = classDict['Name']

def AssignHp():
	global level
	global health
	global classDict
	
	conMod = (math.floor((stats[2]-10)/2))
	if conMod < 0:
		conMod = 0
	
	hitDie = classDict['HitDie']
	preDefHpPrLv = int((hitDie/2)+1)
	health = hitDie + conMod
	hpChoise = universal_functions.GetValidOption(1,2,"That is not a valid choise. Please try again: " ,"Do you want to get hp by:\n1.\tRolling it randomly on a d" + str(hitDie) + "\n2.\tChoose the predefined which for your class is: " + str(int(preDefHpPrLv)) + "\nWhat is your choise? ")
	
	if hpChoise == 1:
		for i in range(level-1):
			health += random.randint(1,hitDie) + conMod
	else:
		for i in range(level-1):
			health += preDefHpPrLv + conMod
	print("Your character will start with: " + str(health) + " HP")
	
def GetArmorType():
	global equipment
	global AC
	global stats
	
	dexMod = math.floor((stats[1]-10)/2) if math.floor((stats[1]-10)/2) >=0 else 0
	
	armorChoise = universal_functions.GetValidOption(1,3,"That is not a valid choise of Armor", "There are three armortypes you can choose:\n1.\tLight armor\n2.\tMedium armor\n3.\tHeavy armor\nWhat armortype do you want? ")-1
	
	armorList = [["Padded",11+dexMod],["Hide",12+[dexMod if dexMod <= 2 else 2][0]],["Ring Mail",14]]
	
	equipment.append(armorList[armorChoise][0])
	AC = armorList[armorChoise][1]
	
def RunProgram():	#I make the program structure a function in order to guarrantee that i have defined all required function and variables already


	#importing global variables
	global name
	global level
	global charType
	global resistances
	global stats
	global movementSpeed
	global race
	global subRace
	global size
	global sizeFlavor
	global langs
	global age
	global alignment
	global abilities
	global proficiencies
	global traits
	global charClass
	global health
	global AC
	global equipment
	global profBonus
	
	
	name = input("What do you want to call this character? ")								#every character needs a name
	charType = input("is this character ment to be an monster or a player? m/p ").lower()
	while(charType!= "m" and charType != "p"):											#loop to ensure the player chooses a valid option
		print("you did not choose 'm' or 'p'")
		charType = input("is this character ment to be an monster or a player? m/p ").lower()		
	level = universal_functions.GetValidOption(1,20,"That is not a valid level for a DnD player\nPlease try again ","what level should this character start out as? ")
	statChoiseMethods = [RollStats,PointBuyStats,PredefinedStats]
	statChoiseMethods[universal_functions.GetValidOption(1, 3, "you did not choose 1/2/3. Please try again: ", "How do you want to choose your stats?\n1.\tRoll stats\n2.\tPoint buy\n3.\tPredefined stats\nChoose 1/2/3: ")-1]()
	AssignRace()	
	AssignClass()
	AssignHp()
	AssignAlignment()
	GetArmorType()
	
	profBonus = 1+math.ceil(level/4)
	
	saveCharacter(name, stats, movementSpeed, level, charType, race, resistances, size, sizeFlavor, langs, age, alignment, subRace, abilities, proficiencies, traits, charClass, health, AC, equipment, profBonus)
	os.system('cls')

	