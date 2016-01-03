import io
import string

phraselist = []

def loadphrases():
	f = open("bannable.knu", 'r')
	for line in f:
	
		if "\n" in line:
			line = line.replace("\n", "")
			
		phraselist.insert(1, line)