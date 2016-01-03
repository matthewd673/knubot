import io
import string

commandlist = []

def loadcommands():
	f = open("commands.knu", 'r')
	for line in f:
	
		if "\n" in line:
			line = line.replace("\n", "")
	
		commandlist.insert(1, line)