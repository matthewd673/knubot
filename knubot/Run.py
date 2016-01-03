import string

from Settings import BAND, GBYE, COMM, BANP, CSCO, CSBN, POLL, CSPL, PLEW, PLCO, VTCO, NPMS
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Read import getUser, getMessage
from Commands import loadcommands, commandlist
from Ban import loadphrases, phraselist
from Poll import loadpoll, optionlist

s = openSocket()
joinRoom(s)

#get everything ready to go
loadcommands()
loadphrases()
loadpoll()

readbuffer = ""

cycle = 0

while True:

	readbuffer = readbuffer + s.recv(1024)
	temp = string.split(readbuffer, "\n")
	readbuffer = temp.pop()
	
	for line in temp:

		#refresh everything
		loadcommands()
		loadphrases()
		loadpoll()
		
		cycle = cycle + 1
		print(cycle)
	
		if "PING :tmi.twitch.tv" in line:
			print("Twitch PING'd")
			s.send(line.replace("PING", "PONG"))
			print("Knubot PONG'd")
		else:
			print(line)
			user = getUser(line)
			message = getMessage(line)
			#commands
			if COMM == True:
				for command in commandlist:
				
					separate = command.split(" : ", 1)
					
					if CSCO == True:
						if separate[0] in message:
							sendMessage(s, separate[1])
							print("Command received and returned (" + separate[0] + ", " + separate[1] + ")")
					else:
						if separate[0].lower() in message.lower():
							sendMessage(s, separate[1])
							print("Command received and returned (" + separate[0] + ", " + separate[1] + ")")
					
			#bannable phrases
			if BANP == True:
				for phrase in phraselist:
				
					if CSBN == True:
						if phrase in message:
							sendMessage(s, "/ban " + user)
							print("User " + user + " has been banned for saying " + phrase + ".")
							sendMessage(s, BAND + " (" + user + " has been banned for saying " + phrase + ")")
					else:
						if phrase.lower() in message.lower():
							sendMessage(s, "/ban " + user)
							print("User " + user + " has been banned for saying " + phrase + ".")
							sendMessage(s, BAND + " (" + user + " has been banned for saying " + phrase + ")")
			
			#polls
			if POLL == True:
			
				optionstring = "POLL OPTIONS: "
			
				for option in optionlist:
					
					optionstring = optionstring + option + "; "
						
					#vote on poll
					if VTCO in message:
						if " " in message:
							separate = message.split(" ", 1)
							separateoption = option.split(" : ")
							
							if CSPL == True:
								#case sensitivity on
								if PLEW == True:
									#allow exact phrasing
									if separateoption[0] in separate[1]:
										#numeric poll option found
									if separateoption[1] in separate[1]:
										#exact poll option found
								else:
									#allow numeric options only
									if separateoption[0] in separate[1]:
										#numeric poll option found
							else:
								#case sensitivity off
								if PLEW == True:
									#allow exact phrasing
									if separateoption[0].lower() in separate[1].lower():
										#numeric poll option found
									if separateoption[1].lower() in separate[1].lower():
										#exact poll option found
								else:
									#allow numeric options only
									if separateoption[0].lower() in separate[1].lower():
										#numeric poll option found
		
			else:
				if VTCO in message:
					sendMessage(s, NPMS)
				if PLCO in message:
					sendMessage(s, NPMS)