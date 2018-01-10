Welcome to DnDlike.	Alpha V0.1.2.3B
This is a character creator/battle simulator based on the Dungeons and Dragons mechanics.

Before modifying and distributing be sure to read content in folder "Legal information"

Program made by: Michael Jeppesen
Based on Dungeons and Dragons published by: TSR and Wizardds of the Coast
All content in this program can be found in the 5e srd on: http://www.5esrd.com/ as of 10/10-2017

If you enjoy this content please consider donating to me at: "https://www.paypal.me/SirEraisuithon"

Current content:
	- Character creation (all classes implemented but class features have no effect)
	- Basic combat
	- Create attack spells
	- Diceroller
	
Planned content:
	- Level up system
	- Flush out some kinks in character creation, and possible add some more features
	- Need to make class features have an effect
	- Full combat system
		- Move spells, attacks and consumables out of being hard coded and save them in seperate files
	- Gear/spell etc creation and usage
		- Only need to add gear and buff spells
	- Spell encykopedia (of spells in the spell folder)
	- Possibly other stuff

Changelog:
	Alpha V0.1.2.3B:
		- Bugfix: When creating a spell it now gets added to the attacklist instantly instead of requiering a restart
	
	Alpha V0.1.2.3A:
		- Added an option to show the individual rolls in the diceroller
		
	Alpha V0.1.2.2A:
		- Moved races and subraces from being hard coded into the program to being in txt-files (Meaning they can be made customly by making a new txt file with the correct format)
		- Updated legal information

	Aplha V0.1.2.1A:
		- Added all classes to character creation (but only affects hit die and class name (meaning babarian is the strongest because it has the highest hit dice))

	Aplha V0.1.2.0C:
		- Fixed bug in diceroller where negative modifyers would add to total

	Aplha V0.1.2.0B:
		- Made notation clearer and added negative modifyers in the diceroller

	Alpha V0.1.2.0A:
		- Implemented a diceroller
		
	Alpha V0.1.1.0A:
		- You can now create your own spells in the "Create equipment, spells or alike" section (although only attacking spells)

	Alpha V0.1.0.1B:
		- Removed some debugging text
		
	Alpha V0.1.0.1A:
		- Decentralized attacks from being hard-coded in solo_encount.py to be seperate programs in Resources/Spells
		- Moved often used functions to a central program (universal_functions.py)
		- Updated Legal-information

	Alpha V0.1.0.0A:
		- Created base program stucture
		- Implemented character creation
		- Implemented the rudementaries of combat
		- Created data structure
		- Created Legal-information