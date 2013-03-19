#!/usr/bin/env python
import socket
import sys
import getpass

#Messages to be transmitted over server
passerror = ('Password incorrect, please try again')


def statusMessage():
        global AlarmStatus
        global AlarmActive
        global alarmMessage
        lines = tuple(open('alarm.txt', encoding='utf-8', mode = 'r'))
        AlarmActive = lines[0]
        AlarmStatus = lines[1]
        alarmMessage =("Alarm Status:" + AlarmStatus + "\nAlarm Active:" +AlarmActive)

# Function that will either take the second command line argument has the server address or will ask the user to input one into the terminal
def serverAdd():
	global serverAdd
	if len(sys.argv) <2:
		serverAdd = input('Please enter server address:')
	else:
		serverAdd = sys.argv[1]

# Function that will either take the third command line argument has the port number for this server to run on or will ask the user to input one into the terminal
def serverPort():
	global portNumber
	if len(sys.argv) <3:
		portNumber = int(input('Please enter port number for server:'))
	else:
		portNumber = sys.argv[2]
		portNumber =int(portNumber)
		
# Function that will take the fourth command line argument as the password for the server, if no password is present user will be asked to input one via the terminal		
def serverPassword():
	global password
	if len(sys.argv)< 4:
		password = input('Please enter server password:')
	else:
		password = sys.argv[3]

# Function that deals with reading and decoding password send over from user and then stores this has a global variable 
def authClient():
	global clientpass
	print ('Authenticating')
	clientpass = connection.recv(1024)
	clientpass = clientpass.decode('utf-8')
	clientpass= str(clientpass)
	
# Function that will either send detils of the alarm to the client if the password matches that of the server. If this password is incorrect a password error message will be sent to the client
def sendMessage():
	if clientpass == password:
		print('Password Accepted')
		print('Sending data to', client_address)
		statusMess()
		connection.sendall(alarmMessage.encode('utf-8'))
		print('Finished sending data to', client_address)
	else:
		connection.sendall(passerror.encode('utf-8'))
		print('Password recieved from', client_address, 'is incorrect')
		
	
# Set up the server address, port and password		
serverAdd()
serverPort()
serverPassword()
server_address =(serverAdd, portNumber)

# Bind sever address to socket
sock.bind(server_address)

# Listen for connections, will only allow one connection to take place
sock.listen(1)


#control loop for server
while True:
	
	print ('Waiting for a connection')
	connection, client_address = sock.accept()
	try:
		print ('connection from', client_address)
		while True:
			authClient()
			sendMessage()
			break
	finally:
		connection.close()




		
	
	
