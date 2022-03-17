import socket
serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
	try:
		message = input('# ')
	except EOFError as e:
		break
	clientSocket.sendto(bytes(message, 'utf-8'), (serverName, serverPort))
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print(modifiedMessage.decode())
	
	
clientSocket.close()
#CLIENT

