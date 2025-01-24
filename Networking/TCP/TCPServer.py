from socket import *

serverPort = 
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))

##server listen for TCP connection requests from the client
##The parameter specifies the maximum number of queued connections (at least 1).
serverSocket.listen(1)

print('The server is ready to receive')

while True:
# When a client knocks on this door, the program invokes the accept() method for
# serverSocket, which creates a new socket in the server, called connectionSocket,
# dedicated to this particular client.
    connectionSocket, addr = serverSocket.accept()
    
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
# after sending the modified sentence to the client, we close the con-
# nection socket. But since serverSocket remains open, another client can now
# knock on the door and send the server a sentence to modify.
    connectionSocket.close()