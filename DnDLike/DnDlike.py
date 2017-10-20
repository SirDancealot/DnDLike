from Scripts import create_character
from Scripts import solo_encounter
from Scripts import level_up
from Scripts import create_misc
from Scripts import diceroller
from Scripts import universal_functions
import os

def AssignDicts():
	level_up.AssignDicts()
	create_character.AssignDicts()

AssignDicts()
programs = [create_character, create_misc, level_up, solo_encounter, diceroller]
numOfScripts = len(programs)
playing = True
print("Welcome to DnDlike, the best battle sim and character creater for DnD there is, maybe.")
while(playing):
	option = universal_functions.GetValidOption(1, numOfScripts+1, "That is not a valid option. Please try again: ", "Do you want to:\n1.\tCreate a character\n2.\tCreate equipment, spells or alike\n3.\tLevel up a character\n4.\tPlay an encounter with a character\n5.\tUse the diceroller\n6.\tStop the program\nPlease choose: ")
	if option > numOfScripts:
		playing = False
	else:
		os.system('cls')
		programs[option-1].RunProgram()
input("The program is now closing, thank you for playing\nIf you enjoyed you may consider donating at 'https://www.paypal.me/SirEraisuithon'")