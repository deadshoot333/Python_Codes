from socket import *

##server initialization
serverName = '192.168.0.101' ##my device ip address
serverPort =1200

##socket creation
##AF_INET indicates that underlying network is using IPV4
##SOCK_DGRAM means it is a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

##enter your message
message = input("Input lowercase sentence:")

##message.encode()-> convert string to bytes
##(serverName,serverPort)-> tuple about the server
clientSocket.sendto(message.encode(), (serverName, serverPort))

##2048 is buffer size
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

##serverAddress is a tuple which is indexed by [0],[1]
print(f"Message modified from Server Name:{serverAddress[0]}\nServer Port:{serverAddress[1]}")

##socket is closed
clientSocket.close()
