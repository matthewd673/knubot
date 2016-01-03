import socket
from Settings import HOST, PORT, PASS, NICK, CHAN

def openSocket():
	
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send("PASS " + PASS + "\r\n") #send password
	s.send("NICK " + NICK + "\r\n") #send username
	s.send("JOIN #" + CHAN + "\r\n") #join channel
	return s
	
def sendMessage(s, message):
	
	messageTemp = "PRIVMSG #" + CHAN + " :" + message #message looks like ->  PRIVMSG #CHAN :Message content
	s.send(messageTemp + "\r\n")
	print("Sent: " + messageTemp)