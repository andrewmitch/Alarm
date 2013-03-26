#!/usr/bin/env python

import sys
import socket
import ipaddress
import getpass

#Create socket for client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Function that will take the second command line argument as the server address or will request the user to input the address should no such argument be present.
def serverAdd():
    global serverAddress
    while True:
        try:
            serverAddress = input('Please enter server address:')
            return ipaddress.ip_address(serverAddress)
        except ValueError:
            print("Not a Valid IP address")
            
# Function that will check if there is port number passed as an command line arument or request the user to input one should none be present. Must be of type int.
def serverPort():
    global portNumber
    while True:
        try:
            portNumber = int(input('Please enter port number for server:'))
            return int(portNumber)
        except ValueError:
            print("Not a valid port number")
        
# Function that will either take the fourth command argument input as a password or request one from the user should no password be present.
def serverPassword():
    global serverPass
    while True:
        try:
            serverPass =getpass.getpass('Please enter password for the server:')
            if len(serverPass) <=4:
                print('Password too short, please enter a more approiate password.')
            else:
                return(serverPass)
        except ValueError:
            print("Error occurred, when entering password")
       
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
