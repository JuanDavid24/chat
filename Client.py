from socket import *
import pickle

serverPort = 12000
CSocket = socket(AF_INET, SOCK_STREAM)
CSocket.connect(('', serverPort))
print("Conectado al servidor")
destiny = input("ID del usuario de destino:")
messageToSend = input("escriba mensaje:")

#Enviar
packToSend = [destiny,messageToSend]
dataToSend = pickle.dumps(packToSend)
#print (packet)
CSocket.send(dataToSend)

#Recibir
PackRecv = CSocket.recv(1024)
dataRecv = pickle.loads(PackRecv)
SenderID = dataRecv[0]
messageRecv = dataRecv[1]
print ("User " + SenderID + ": " + messageRecv)