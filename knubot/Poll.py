import io
import string

optionlist = []

def loadpoll():
	f = open("poll.knu", 'r')
	for line in f:
	
		if "\n" in line:
			line = line.replace("\n", "")
	
		optionlist.insert(1, line)