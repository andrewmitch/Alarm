#!/usr/bin/env python

import sys
import socket
import ipaddress

#Create socket for client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Function that will take the second command line argument as the server address or will request the user to input the address should no such argument be present.
def serverAdd():
    global serverAddress
    if len(sys.argv) <2:
        serverAddress = input('Please enter server address:')
    else:
        serverAddress = sys.argv[1]
    try:
        return ipaddress.ip_address(serverAddress)
    except ValueError:
        print("Not a Valid IP address")
        serverAdd()

# Function that will check if there is port number passed as an command line arument or request the user to input one should none be present. Must be of type int.
def serverPort():
    global portNumber
    if len(sys.argv) <3:
        portNumber = int(input('Please enter port number for server:'))
    else:
        portNumber = sys.argv[2]
        portNumber =int(portNumber)
        
# Function that will either take the fourth command argument input as a password or request one from the user should no password be present.
def serverPassword():
    global serverPass
    if len(sys.argv) <4:
        serverPass = input('Please enter password for the server:')
        #serverPass = getpass.getpass('Please enter the server password:')
    else:
        serverPass = sys.argv[3]

# Call functions that relate to server details
serverAdd()
serverPort()
serverPassword()
server_address = (serverAddress, portNumber)
print ('connecting to %s on port %s' % server_address)

# Connect this client socket to the server
sock.connect(server_address)
passwordMsg = str(serverPass)

try:
        sock.sendall(passwordMsg.encode('utf-8'))
        data = sock.recv(1024)
        print(data.decode('utf-8'))
finally:
        print('closing socket')
        sock.close()
