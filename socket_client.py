# Code modified from: realpython.com/python_sockets

# Author: miti@phas.ubc.ca
# Created on: 2024-01-10

import socket

HOST = "127.0.0.1" # address of the server (local host in this case)
PORT = 65432 # port of the server

# SOCK_STREAM: specifies socket uses TCP 
# SOCK_DGRAM: specifies socket uses UDP 
# AF_INET: specifies socket uses IPv4 
                                                                                
# Using "with" make it so the client_socket.close() is called automatically 
# when program is outside the scope of the with statement. 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT)) # connects to the server
    client_socket.sendall(b"Hello world") # send data to server
    data = client_socket.recv(1024) # receive data from server

print(f"Received {data!r}")

