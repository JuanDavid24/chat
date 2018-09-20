from socket import *
import pickle #Para poder enviar y recibir listas por sockets

SPort = 12000
SSocket = socket (AF_INET, SOCK_STREAM)
SSocket.bind(('',SPort))
SSocket.listen(1)

users = []

while 1:
	print ("Chat server is ready")

	#Acepta conexión
	connectionSocket, addr = SSocket.accept()
	users.append(connectionSocket)

	#Recibe
	packet = users[0].recv(1024)
	data = pickle.loads(packet)
	print (data)

	#Envía
	userTo = int(data[0])
	message = data[1]
	print(userTo)
	print(message)
	users[userTo].send(packet)
