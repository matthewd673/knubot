import string
from Socket import sendMessage
from Settings import WELC

def joinRoom(s):
	readbuffer = ""
	loading = True
	
	while loading:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			loading = loadingComplete(line)
			
	sendMessage(s, WELC)
	
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True