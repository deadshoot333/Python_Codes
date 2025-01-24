##server must run before client in a sperate terminal
from socket import *

serverPort = 1200
serverSocket = socket(AF_INET, SOCK_DGRAM)

##assigns port to socket
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    ##convert bytes to string using decode and CAPITALIZE it using upper()
    modifiedMessage = message.decode().upper()
    print(f'Message receive from Client Address:{clientAddress[0]}\nClient Port:{clientAddress[1]}')
    print(f'Message changed to {modifiedMessage}')
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)