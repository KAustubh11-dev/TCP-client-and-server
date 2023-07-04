import socket
import threading
import time


port=7007
server = socket.gethostbyname(socket.gethostname())
address=(server,port)


cl_socket = socket.socket()             #socketcreation
cl_socket.connect(address)       #connecting Client socket to server
print('Connected to server {}:{}'.format(server,port))

data = 'SetA-One'
cl_socket.send(data.encode())

response = cl_socket.recv(7007).decode()
print('Received:', response)                #recive data from server

cl_socket.close()