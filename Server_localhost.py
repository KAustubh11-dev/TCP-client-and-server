import socket
import time
import threading

port=7007
server = socket.gethostbyname(socket.gethostname())

Address =(server, port)


server_socket = socket.socket()       #socket created
server_socket.bind(Address)

server_socket.listen(5)
print("Waiting for connection ", Address)


server_collection = {
    "SetA-One": 1,
    "SetB-Two": 2,
    "SetC-Three": 3,
    "SetD-Four": 4,
    "SetE-Five": 5
}

while True:

    cl_socket, cl_address = server_socket.accept()
    print('Server connected to :', cl_address)

    data = cl_socket.recv(7007).decode()
    print('Received data from client:', data)

    if data in server_collection:
        value=server_collection[data]

#send time at value
    for _ in range(value):
            current_time = time.ctime(time.time())
            cl_socket.send(current_time.encode())
            time.sleep(1)
    else:
        cl_socket.send('NA'.encode())
    

cl_socket.close()