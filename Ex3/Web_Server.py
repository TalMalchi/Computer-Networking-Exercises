# import socket module
import socket
from socket import *
import sys  # In order to terminate the program

if __name__ == '__main__':

    serverSocket = socket(AF_INET, SOCK_STREAM)
    #Binding Socket to port 6789 and puts its in listen mode to allow 1 connection.
    serverSocket.bind(("", 6789))
    serverSocket.listen(1)
    # Fill in end
    while True:
        # Establish the connection
        print('Ready to serve...')
        # Accepting Connection from client. Return a tuple of client socket and address.
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1] if message.split().__len__() > 1 else None
            f = open(filename[1:])
            outputdata = f.read()
            # Send one HTTP header line into socket
            connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
            connectionSocket.send('Content-Type: text/html\r\n'.encode())
            connectionSocket.send('\r\n'.encode())
            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()

        except IOError:
            # Send response message for file not found
            connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
            # Close client socket
            connectionSocket.close()

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data
