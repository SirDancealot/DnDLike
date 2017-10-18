import os
files = []
for x in os.listdir("Resources/Spells"):
	if x.lower().endswith(".py"):
		files.append(x.split(".")[0])

__all__ = files