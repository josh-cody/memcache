from socket import *
import sys
import json


with open('data.json') as d_file:
	dictionary = json.load(d_file)


def get(key):
	return dictionary.get(key)
	
def set(key, val):
	dictionary.update({key : val})
	if dictionary.get(key) == val: return True
	return False
	
serverPort = int(sys.argv[1])
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("localhost", serverPort))
print("The server is ready to recieve")

while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	decodedMessage = message.decode()
	
	commandList = decodedMessage.split(' ')

	for x in commandList:
		if x == '\\r\\n' or x == '\n':
			commandList.remove(x)
	toSend = ''
	if commandList[0] == 'get':
			toSend = 'VALUE ' + str(commandList[1]) + " " + str(len(get(commandList[1]))) + "\r\n" + str(get(commandList[1]))
		
	elif commandList[0] == 'set':
		if len(commandList) >= 4:
			if set(commandList[1], commandList[3]):
				toSend = 'STORED\r\n'
				d_file = open("data.json", "w")
				json.dump(dictionary, d_file)
				d_file.close()
			else:
				toSend = 'NOT-STORED\r\n'
		else:
			toSend = "NOT-A-COMMAND\r\n"
	else:
		toSend = "NOT-A-COMMAND\r\n"
	serverSocket.sendto(toSend.encode(), clientAddress)
#SERVER

